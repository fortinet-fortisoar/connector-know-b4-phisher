"""
Copyright start
MIT License
Copyright (c) 2024 Fortinet Inc
Copyright end
"""
import json

from requests import request, exceptions as req_exceptions
from connectors.core.connector import get_logger, ConnectorError
from .constants import *


logger = get_logger("know-b4-phisher")


class KnowB4PhishER:
    def __init__(self, config, *args, **kwargs):
        server_url = config.get("server_url").strip('/')
        if not server_url.startswith('https://') and not server_url.startswith('http://'):
            server_url = "https://" + server_url
        self.url = server_url
        self.api_key = config.get("api_key")
        self.verify_ssl = config.get("verify_ssl")

    def api_request(self, method="POST", data=None):
        try:
            headers = {"Authorization": f"Bearer {self.api_key}"}
            logger.error(f"\n-----------req-------------\n{method} - {self.url}\nheaders: {headers}\ndata: {data}")
            return {}
            response = request(method, self.url, headers=headers, data=data, verify=self.verify_ssl)

            if response.ok:
                return response.json()
            else:
                if response.text != "":
                    err_resp = response.text
                    error_msg = 'Response [{0}:{1}]'.format(response.status_code, err_resp)
                else:
                    error_msg = 'Response [{0}:{1}]'.format(response.status_code, response.content)
                logger.error(error_msg)
                raise ConnectorError(error_msg)
        except req_exceptions.SSLError:
            logger.error('An SSL error occurred')
            raise ConnectorError('An SSL error occurred')
        except req_exceptions.ConnectionError:
            logger.error('A connection error occurred')
            raise ConnectorError('A connection error occurred')
        except req_exceptions.Timeout:
            logger.error('The request timed out')
            raise ConnectorError('The request timed out')
        except req_exceptions.RequestException:
            logger.error('There was an error while handling the request')
            raise ConnectorError('There was an error while handling the request')
        except Exception as err:
            raise ConnectorError(str(err))


def create_request_payload(readable_request):
    format_desc = readable_request.splitlines()
    final = ""
    for line in format_desc:
        final += line + '\\n'
    return final[:-2]


def convert_to_list(value):
    if not value:
        return value
    elif isinstance(value, list):
        return [x.strip() for x in value]
    elif isinstance(value, str):
        return [x.strip() for x in value.split(",")]


def get_message_list(config, params):
    ob = KnowB4PhishER(config)
    query = params.get("query")
    fetch_all = params.get("all") or False
    page = params.get("page") or 1
    per = params.get("per") or 25
    message_id = params.get("id")
    query = '\"\"' if not query else f'\"{query}\"'
    if message_id:
        query = f'\"id:{message_id}\"'
        fetch_all = False
        page = 1
        per = 25
    query = query.lower()
    payload_init = GET_MESSAGE_PAYLOAD.format(fetch_all, page, per, query)
    payload = json.dumps({'query': payload_init, 'variables': {}})
    updated_payload = create_request_payload(payload)
    result = ob.api_request(data=updated_payload)
    return result


def update_message(config, params):
    ob = KnowB4PhishER(config)
    message_id = params.get('id')
    category = params.get('category')
    status = params.get('status')
    severity = params.get('severity')
    attributes = {}
    category and attributes.update(category=CATEGORY_MAPPING[category])
    status and attributes.update(status=STATUS_MAPPING[status])
    severity and attributes.update(severity=SEVERITY_MAPPING[severity])
    if not attributes:
        raise ConnectionError("At least one of the following argument must be provided: Category, Status, Severity")
    attr_str = json.dumps(attributes)
    attr_str = attr_str.replace('\"', '')
    attr_str = attr_str.replace(' ', '')
    payload = UPDATE_MESSAGE_PAYLOAD.format(message_id, attr_str)
    final = json.dumps({'query': payload, 'variables': {}})
    final_req = create_request_payload(final)
    result = ob.api_request(data=final_req)
    errors = result.get('data', {}).get('phisherCommentCreate', {}).get('errors', "")
    if not errors:
        return {"message": "success"}
    else:
        raise ConnectorError(str(errors))


def add_comment(config, params):
    ob = KnowB4PhishER(config)
    message_id = params.get("id")
    comment = params.get("comment")
    payload = ADD_COMMENT_PAYLOAD.format(comment, message_id)
    final = json.dumps({'query': payload, 'variables': {}})
    final_str = create_request_payload(final)
    result = ob.api_request(data=final_str)
    errors = result.get('data', {}).get('phisherCommentCreate', {}).get('errors', "")
    if not errors:
        return {"message": "success"}
    else:
        raise ConnectorError(str(errors))


def add_tags(config, params):
    ob = KnowB4PhishER(config)
    message_id = params.get('id')
    tags = convert_to_list(params.get('tags')) or []
    parsed_tags = ""
    for tag in tags:
        if not parsed_tags:
            parsed_tags = f'\"{tag}\"'
        else:
            parsed_tags = f'{parsed_tags}, \"{tag}\"'
    payload = ADD_TAGS_PAYLOAD.format(message_id, parsed_tags)
    final = json.dumps({'query': payload, 'variables': {}})
    final_req = create_request_payload(final)
    result = ob.api_request(data=final_req)
    errors = result.get('data', {}).get('phisherTagsCreate', {}).get('errors', "")
    if not errors:
        return {"message": "success"}
    else:
        raise ConnectorError(str(errors))


def remove_tags(config, params):
    ob = KnowB4PhishER(config)
    message_id = params.get('id')
    tags = convert_to_list(params.get('tags'))
    parsed_tags = ""
    for tag in tags:
        if not parsed_tags:
            parsed_tags = f'\"{tag}\"'
        else:
            parsed_tags = f'{parsed_tags}, \"{tag}\"'
    payload = REMOVE_TAGS_PAYLOAD.format(message_id, parsed_tags)
    final = json.dumps({'query': payload, 'variables': {}})
    final_req = create_request_payload(final)
    result = ob.api_request(data=final_req)
    errors = result.get('data', {}).get('phisherTagsDelete', {}).get('errors', "")
    if not errors:
        return {"message": "success"}
    else:
        raise ConnectorError(str(errors))


def check_health_ex(config):
    get_message_list(config, {})
    return True


operations = {
    "get_message_list": get_message_list,
    "update_message": update_message,
    "add_comment": add_comment,
    "add_tags": add_tags,
    "remove_tags": remove_tags
}
