"""
Copyright start
MIT License
Copyright (c) 2024 Fortinet Inc
Copyright end
"""

GET_MESSAGES_PAYLOAD = """
query ($query: String!, $all: Boolean, $page: Int, $per: Int) {
  phisherMessages(query: $query, all: $all, page: $page, per: $per) {
    nodes {
      actionStatus
      attachments {
        actualContentType
        filename
        md5
        reportedContentType
        s3Key
        sha1
        sha256
        size
        ssdeep
        virustotal {
          permalink
          positives
          scanned
          sha256
        }
      }
      category
      comments {
        body
        createdAt
      }
      events {
        causer
        createdAt
        eventType
        events {
          ...on PhisherEventCrowdstrikeDetonationResult {
            detonation
            identifier
            permalink
            scanDate
            threatScore
            type
            verdict
          }
          ...on PhisherEventCrowdstrikeDetonationRun {
            identifierNonNull: identifier
            type
          }
          ...on PhisherEventCrowdstrikeScanResult {
            autoscan
            identifierNonNull: identifier
            maliciousConfidence
            permalinkNonNull: permalink
            scanDateNonNull: scanDate
            type
          }
          ...on PhisherEventCrowdstrikeScanRun {
            identifierNonNull: identifier
            type
          }
          ...on PhisherEventEmails {
            emails {
              actionEmailId
              email
              status
              to
            }
          }
          ...on PhisherEventEvaluatorEnqueued {
            details
            traceSpan
          }
          ...on PhisherEventFieldChanges {
            changes {
              from
              name
              to
            }
          }
          ...on PhisherEventPhishFlipTemplateStatus {
            kmsatTemplate
          }
          ...on PhisherEventPhishML {
            clean
            spam
            threat
          }
          ...on PhisherEventPhishRipCompleted {
            end
            quarantine
            read
            results
            start
            users
          }
          ...on PhisherEventPhishRipFailed {
            queriedFields
          }
          ...on PhisherEventPhishRipStarted {
            end
            quarantine
            start
          }
          ...on PhisherEventReplayComplete {
            complete
          }
          ...on PhisherEventReplayTriggered {
            runActions
          }
          ...on PhisherEventSyslog {
            name
          }
          ...on PhisherEventTag {
            added
            removed
          }
          ...on PhisherEventVirusTotalResult {
            identifierNonNull: identifier
            permalinkNonNull: permalink
            positives
            scanDateNonNull: scanDate
            scanned
            type
          }
          ...on PhisherEventVirusTotalRun {
            identifierNonNull: identifier
            type
          }
          ...on PhisherEventWebhook {
            name
          }
          ...on PhisherEventWebrootScanResult {
            age
            categories
            country
            identifierNonNull: identifier
            popularity
            reputation
            scanDateNonNull: scanDate
            threatHistory
            type
          }
          ...on PhisherEventWebrootScanRun {
            identifierNonNull: identifier
            type
          }
        }
        id
        triggerer
      }
      from
      headers {
        data
        header
        order
      }
      id
      links {
        dispositions
        firstSeen
        id
        lastSeen
        scheme
        target
        url
        virustotal {
          permalink
          positives
          scanned
          sha256
        }
      }
      phishmlReport {
        confidenceClean
        confidenceSpam
        confidenceThreat
      }
      pipelineStatus
      rawUrl
      reportedBy
      rules {
        createdAt
        description
        id
        matchedCount
        name
        tags
      }
      severity
      subject
      tags {
        name
        type
      }
    }
    pagination {
      page
      pages
      per
      totalCount
    }
  }
}"""

GET_MESSAGE_BY_ID_PAYLOAD = """
query GetPhisherMessage($id: String!) {
  phisherMessage(id: $id) {
    actionStatus
    attachments {
      actualContentType
      filename
      md5
      reportedContentType
      s3Key
      sha1
      sha256
      size
      ssdeep
      virustotal {
        permalink
        positives
        scanned
        sha256
      }
    }
    category
    comments {
      body
      createdAt
    }
    events {
      causer
      createdAt
      eventType
      events {
        ...on PhisherEventCrowdstrikeDetonationResult {
          detonation
          identifier
          permalink
          scanDate
          threatScore
          type
          verdict
        }
        ...on PhisherEventCrowdstrikeDetonationRun {
          identifierNonNull: identifier
          type
        }
        ...on PhisherEventCrowdstrikeScanResult {
          autoscan
          identifierNonNull: identifier
          maliciousConfidence
          permalinkNonNull: permalink
          scanDateNonNull: scanDate
          type
        }
        ...on PhisherEventCrowdstrikeScanRun {
          identifierNonNull: identifier
          type
        }
        ...on PhisherEventEmails {
          emails {
            actionEmailId
            email
            status
            to
          }
        }
        ...on PhisherEventEvaluatorEnqueued {
          details
          traceSpan
        }
        ...on PhisherEventFieldChanges {
          changes {
            from
            name
            to
          }
        }
        ...on PhisherEventPhishFlipTemplateStatus {
          kmsatTemplate
        }
        ...on PhisherEventPhishML {
          clean
          spam
          threat
        }
        ...on PhisherEventPhishRipCompleted {
          end
          quarantine
          read
          results
          start
          users
        }
        ...on PhisherEventPhishRipFailed {
          queriedFields
        }
        ...on PhisherEventPhishRipStarted {
          end
          quarantine
          start
        }
        ...on PhisherEventReplayComplete {
          complete
        }
        ...on PhisherEventReplayTriggered {
          runActions
        }
        ...on PhisherEventSyslog {
          name
        }
        ...on PhisherEventTag {
          added
          removed
        }
        ...on PhisherEventVirusTotalResult {
          identifierNonNull: identifier
          permalinkNonNull: permalink
          positives
          scanDateNonNull: scanDate
          scanned
          type
        }
        ...on PhisherEventVirusTotalRun {
          identifierNonNull: identifier
          type
        }
        ...on PhisherEventWebhook {
          name
        }
        ...on PhisherEventWebrootScanResult {
          age
          categories
          country
          identifierNonNull: identifier
          popularity
          reputation
          scanDateNonNull: scanDate
          threatHistory
          type
        }
        ...on PhisherEventWebrootScanRun {
          identifierNonNull: identifier
          type
        }
      }
      id
      triggerer
    }
    from
    headers {
      data
      header
      order
    }
    id
    links {
      dispositions
      firstSeen
      id
      lastSeen
      scheme
      target
      url
      virustotal {
        permalink
        positives
        scanned
        sha256
      }
    }
    phishmlReport {
      confidenceClean
      confidenceSpam
      confidenceThreat
    }
    pipelineStatus
    rawUrl
    reportedBy
    rules {
      createdAt
      description
      id
      matchedCount
      name
      tags
    }
    severity
    subject
    tags {
      name
      type
    }
  }
}
"""

UPDATE_MESSAGE_PAYLOAD = """
mutation ($id : String!, $payload: MessageUpdateAttributes!){
  phisherMessageUpdate(id: $id, payload: $payload) {
    errors {
      field
      placeholders
      reason
      recordId
    }
    node{
        id
        category
        actionStatus
        severity
    }
  }
}
"""

ADD_COMMENT_PAYLOAD = """
mutation ($comment : String!, $id: String!){
  phisherCommentCreate(comment: $comment, id: $id) {
    errors {
      field
      placeholders
      reason
      recordId
    }
    node {
      body
      createdAt
    }
  }
}
"""

ADD_TAGS_PAYLOAD = """
mutation ($id: String!, $tags: [String!]!){
  phisherTagsCreate(id: $id, tags: $tags) {
    errors {
      field
      placeholders
      reason
      recordId
    }
    nodes {
      name
      type
    }
  }
}
"""

REMOVE_TAGS_PAYLOAD = """
mutation ($id: String!, $tags: [String!]!){
  phisherTagsDelete(id: $id, tags: $tags) {
    errors {
      field
      placeholders
      reason
      recordId
    }
    nodes {
      name
      type
    }
  }
}
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
