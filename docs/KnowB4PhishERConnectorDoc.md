## About the connector
KnowB4 PhishER helps your InfoSec and Security Operations team cut through the inbox noise and respond to the most dangerous threats more quickly.
<p>This document provides information about the KnowB4 PhishER Connector, which facilitates automated interactions, with a KnowB4 PhishER server using FortiSOAR&trade; playbooks. Add the KnowB4 PhishER Connector as a step in FortiSOAR&trade; playbooks and perform automated operations with KnowB4 PhishER.</p>

### Version information

Connector Version: 1.0.0


Authored By: Fortinet

Certified: No
## Installing the connector
<p>Use the <strong>Content Hub</strong> to install the connector. For the detailed procedure to install a connector, click <a href="https://docs.fortinet.com/document/fortisoar/0.0.0/installing-a-connector/1/installing-a-connector" target="_top">here</a>.</p><p>You can also use the <code>yum</code> command as a root user to install the connector:</p>
<pre>yum install cyops-connector-know-b4-phisher</pre>

## Prerequisites to configuring the connector
- You must have the credentials of KnowB4 PhishER server to which you will connect and perform automated operations.
- The FortiSOAR&trade; server should have outbound connectivity to port 443 on the KnowB4 PhishER server.

## Minimum Permissions Required
- Not applicable

## Configuring the connector
For the procedure to configure a connector, click [here](https://docs.fortinet.com/document/fortisoar/0.0.0/configuring-a-connector/1/configuring-a-connector)
### Configuration parameters
<p>In FortiSOAR&trade;, on the Connectors page, click the <strong>KnowB4 PhishER</strong> connector row (if you are in the <strong>Grid</strong> view on the Connectors page) and in the <strong>Configurations</strong> tab enter the required configuration details:</p>
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Server URL</td><td>Specify the server URL to connect and perform the automated operations.
</td>
</tr><tr><td>API Key</td><td>API key to access the endpoint to connect and perform the automated operations
</td>
</tr><tr><td>Verify SSL</td><td>Specifies whether the SSL certificate for the server is to be verified or not. <br/>By default, this option is set to True.</td></tr>
</tbody></table>

## Actions supported by the connector
The following automated operations can be included in playbooks and you can also use the annotations to access operations from FortiSOAR&trade; release 4.10.0 and onwards:
<table border=1><thead><tr><th>Function</th><th>Description</th><th>Annotation and Category</th></tr></thead><tbody><tr><td>Get Messages</td><td>Retrieves the detailed list of messages based on the parameters that you have specified.</td><td>get_message_list <br/>Investigation</td></tr>
<tr><td>Update Message</td><td>Update a message based on the parameters that you have specified.</td><td>update_message <br/>Investigation</td></tr>
<tr><td>Add Comment</td><td>Add comment based on the parameters that you have specified.</td><td>add_comment <br/>Investigation</td></tr>
<tr><td>Add Tags</td><td>Add tags to a message based on the parameters that you have specified.</td><td>add_tags <br/>Investigation</td></tr>
<tr><td>Remove Tags</td><td>Remove tags from a message based on the parameters that you have specified.</td><td>remove_tags <br/>Investigation</td></tr>
</tbody></table>

### operation: Get Messages
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Query</td><td>Specify the lucene query to search and filter the results.
</td></tr><tr><td>Message ID</td><td>Specify the message ID to fetch the result.
</td></tr><tr><td>Fetch All Records</td><td>Select the checkbox to fetch all records at once.
</td></tr><tr><td>Page Number</td><td>Specify the page number from which to retrieve the records. The default value is 1.
</td></tr><tr><td>Page Size</td><td>Specify the number of records that the operation should fetch per page. The minimum value is 25.
</td></tr></tbody></table>

#### Output

 The output contains a non-dictionary value.
### operation: Update Message
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Message ID</td><td>Specify the ID of the message that you want to update.
</td></tr><tr><td>Category</td><td>Specify the category of the message that you want to update.
</td></tr><tr><td>Status</td><td>Specify the status of the message that you want to update.
</td></tr><tr><td>Severity</td><td>Specify the severity of the message that you want to update.
</td></tr></tbody></table>

#### Output

 The output contains a non-dictionary value.
### operation: Add Comment
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Message ID</td><td>Specify the message ID for which you want to add the comment.
</td></tr><tr><td>Comment</td><td>Specify the comment that you want to add.
</td></tr></tbody></table>

#### Output

 The output contains a non-dictionary value.
### operation: Add Tags
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Message ID</td><td>Specify the message ID for which you want to add the tags.
</td></tr><tr><td>Tags</td><td>Specify the comma separated value of the tags that you want to add. eg: Tag1,Tag2
</td></tr></tbody></table>

#### Output

 The output contains a non-dictionary value.
### operation: Remove Tags
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Message ID</td><td>Specify the message ID for which you want to remove the tags.
</td></tr><tr><td>Tags</td><td>Specify the comma separated value of the tags that you want to remove. eg: Tag1,Tag2
</td></tr></tbody></table>

#### Output

 The output contains a non-dictionary value.
## Included playbooks
The `Sample - know-b4-phisher - 1.0.0` playbook collection comes bundled with the KnowB4 PhishER connector. These playbooks contain steps using which you can perform all supported actions. You can see bundled playbooks in the **Automation** > **Playbooks** section in FortiSOAR&trade; after importing the KnowB4 PhishER connector.

- Get Messages
- Update Message
- Add Comment
- Add Tags
- Remove Tags

**Note**: If you are planning to use any of the sample playbooks in your environment, ensure that you clone those playbooks and move them to a different collection since the sample playbook collection gets deleted during connector upgrade and delete.
