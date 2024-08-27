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
            headers = {
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json"
            }
            try:
                from connectors.debug_utils.curl_script import make_curl
                make_curl(method, self.url, headers=headers, data=data, verify_ssl=self.verify_ssl)
            except Exception:
                pass
            response = request(method, self.url, headers=headers, data=data, verify=self.verify_ssl)
            logger.info(f"response status code: {response.status_code}")

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


def get_params(params):
    new_params = {}
    for k, v in params.items():
        if v is False or v == 0 or v:
            new_params[k] = v
    logger.info(f"updated params are: {new_params}")
    return new_params


def convert_to_list(value):
    if not value:
        return value
    elif isinstance(value, list):
        return [x.strip() for x in value]
    elif isinstance(value, str):
        return [x.strip() for x in value.split(",")]


def get_message_list(config, params):
    ob = KnowB4PhishER(config)
    params = get_params(params)
    query = params.get("query")
    query = "" if not query else query
    params.update(query=query)
    data_query = {"query": GET_MESSAGES_PAYLOAD, "variables": params}
    result = ob.api_request(data=json.dumps(data_query))
    return result


def get_message_by_id(config, params):
    ob = KnowB4PhishER(config)
    params = get_params(params)
    data_query = {"query": GET_MESSAGE_BY_ID_PAYLOAD, "variables": params}
    result = ob.api_request(data=json.dumps(data_query))
    return result


def update_message(config, params):
    ob = KnowB4PhishER(config)
    params = get_params(params)
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
    data_query = {"query": UPDATE_MESSAGE_PAYLOAD, "variables": {"id": message_id, "payload": attributes}}
    result = ob.api_request(data=json.dumps(data_query))
    return result


def add_comment(config, params):
    ob = KnowB4PhishER(config)
    params = get_params(params)
    data_query = {"query": ADD_COMMENT_PAYLOAD, "variables": params}
    result = ob.api_request(data=json.dumps(data_query))
    return result


def add_tags(config, params):
    ob = KnowB4PhishER(config)
    params = get_params(params)
    message_id = params.get('id')
    tags = convert_to_list(params.get('tags')) or []
    data_query = {"query": ADD_TAGS_PAYLOAD, "variables": {"id": message_id, "tags": tags}}
    result = ob.api_request(data=json.dumps(data_query))
    return result


def remove_tags(config, params):
    ob = KnowB4PhishER(config)
    params = get_params(params)
    message_id = params.get('id')
    tags = convert_to_list(params.get('tags')) or []
    data_query = {"query": REMOVE_TAGS_PAYLOAD, "variables": {"id": message_id, "tags": tags}}
    result = ob.api_request(data=json.dumps(data_query))
    return result


def check_health_ex(config):
    get_message_list(config, {})
    return True


operations = {
    "get_message_list": get_message_list,
    "get_message_by_id": get_message_by_id,
    "update_message": update_message,
    "add_comment": add_comment,
    "add_tags": add_tags,
    "remove_tags": remove_tags
}
