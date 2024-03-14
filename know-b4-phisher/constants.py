"""
Copyright start
MIT License
Copyright (c) 2024 Fortinet Inc
Copyright end
"""

GET_MESSAGE_PAYLOAD = """query {{
  phisherMessages(all: {}, page: {}, per: {}, query: {}) {{
    nodes {{
      actionStatus
      attachments(status: UNKNOWN) {{
        actualContentType
        filename
        md5
        reportedContentType
        s3Key
        sha1
        sha256
        size
        ssdeep
        virustotal {{
          permalink
          positives
          scanned
          sha256
        }}
      }}
      category
      comments {{
        body
        createdAt
      }}
      events {{
        causer
        createdAt
        eventType
        events {{
          ...on PhisherEventEmails {{
            emails {{
              actionEmailId
              email
              status
              to
            }}
          }}
          ...on PhisherEventFieldChanges {{
            changes {{
              from
              name
              to
            }}
          }}
          ...on PhisherEventPhishFlipTemplateStatus {{
            kmsatTemplate
          }}
          ...on PhisherEventPhishML {{
            clean
            spam
            threat
          }}
          ...on PhisherEventPhishRipCompleted {{
            end
            quarantine
            read
            results
            start
            users
          }}
          ...on PhisherEventPhishRipStarted {{
            end
            quarantine
            start
          }}
          ...on PhisherEventReplayComplete {{
            complete
          }}
          ...on PhisherEventReplayTriggered {{
            runActions
          }}
          ...on PhisherEventSyslog {{
            name
          }}
          ...on PhisherEventTag {{
            added
            removed
          }}
          ...on PhisherEventVirusTotalResult {{
            identifier
            permalink
            positives
            scanDate
            scanned
            type
          }}
          ...on PhisherEventVirusTotalRun {{
            identifierNonNull: identifier
            type
          }}
          ...on PhisherEventWebhook {{
            name
          }}
        }}
        id
        triggerer
      }}
      from
      id
      links(status: UNKNOWN) {{
        dispositions
        firstSeen
        id
        lastSeen
        scheme
        target
        url
        virustotal {{
          permalink
          positives
          scanned
          sha256
        }}
      }}
      phishmlReport {{
        confidenceClean
        confidenceSpam
        confidenceThreat
      }}
      pipelineStatus
      rawUrl
      reportedBy
      rules {{
        createdAt
        description
        id
        matchedCount
        name
        tags
      }}
      severity
      subject
      tags {{
        name
        type
      }}
    }}
    pagination {{
      page
      pages
      per
      totalCount
    }}
  }}
}}"""

UPDATE_MESSAGE_PAYLOAD = """mutation {{
  phisherMessageUpdate(id: \"{}\", payload: {}) {{
    errors {{
      field
      placeholders
      reason
    }}
  }}
}}
"""

ADD_COMMENT_PAYLOAD = """mutation {{
  phisherCommentCreate(comment: \"{}\", id: \"{}\") {{
    errors {{
      field
      placeholders
      reason
    }}
    node {{
      body
      createdAt
    }}
  }}
}}"""

ADD_TAGS_PAYLOAD = """mutation {{
  phisherTagsCreate(id: \"{}\", tags: [{}]) {{
    errors {{
      field
      placeholders
      reason
    }}
  }}
}}
"""

REMOVE_TAGS_PAYLOAD = """mutation {{
   phisherTagsDelete(id: \"{}\", tags: [{}]) {{
    errors {{
      field
      placeholders
      reason
    }}
  }}
}}
"""

CATEGORY_MAPPING = {
    'Unknown': 'UNKNOWN',
    'Clean': 'CLEAN',
    'Spam': 'SPAM',
    'Threat': 'THREAT'
}

STATUS_MAPPING = {
    'Received': 'RECEIVED',
    'In Review': 'IN_REVIEW',
    'Resolved': 'RESOLVED'
}

SEVERITY_MAPPING = {
    'Unknown Severity': 'UNKNOWN_SEVERITY',
    'Low': 'LOW',
    'Medium': 'MEDIUM',
    'High': 'HIGH',
    'Critical': 'CRITICAL'
}
