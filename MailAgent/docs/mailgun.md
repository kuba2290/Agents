Messages
Send email two ways via our REST API:

Send emails using MIME format using a MIME building library
Submit the individual parts (Text, html, attachments, etc.)
Reminder: You can also send email via SMTP with Mailgun. Please reference the user manual.

Send an email
post
/v3/{domain_name}/messages
Pass the components of the messages such as To, From, Subject, HTML and text parts, attachments, etc. Mailgun will build a MIME representation of the message and send it. Note: In order to send you must provide one of the following parameters: 'text', 'html', 'amp-html' or 'template'

Security
basicAuth
Request
path Parameters
domain_name
required
string
Domain name used to send the message

Request Body schema: multipart/form-data
required
from
required
string
Email address for From header

to
required
Array of strings
Email address of the recipient(s). Example: "Bob <bob@host.com>". You can use commas to separate multiple recipients

subject
required
string
Message subject

html
required
string
Body of the message (HTML version)

cc	
Array of strings
Same as To but for Cc

bcc	
Array of strings
Same as To but for Bcc

text	
string
Body of the message (text version)

amp-html	
string
AMP part of the message. Please follow Google guidelines to compose and send AMP emails

attachment	
Array of strings <binary>
File attachment. You can post multiple attachment values. Important: You must use multipart/form-data encoding for sending attachments

inline	
Array of strings <binary>
Attachment with inline disposition. Can be used to send inline images (see example). You can post multiple inline values

template	
string
Name of a template stored via template API to use to render the email body. See Templates for more information

t:version	
string
Render a specific version of the given template instead of the latest version. o:template option must also be provided.

t:text	
string
Render template in case of template sending

Value	Description
yes	Render template in the text part of the message
t:variables	
string
A valid JSON-encoded dictionary used as the input for template variable expansion. See Templates for more information

o:tag	
Array of strings
Tag string. See Tagging for more information

o:dkim	
string
Enables/disables DKIM signatures on a per-message basis

Enum Value	Description
yes	Enables DKIM signatures
no	Disable DKIM signatures
true	Enables DKIM signatures
false	Disable DKIM signatures
o:secondary-dkim	
string
Specify a second domain key to sign the email with. The value is formatted as signing_domain/selector, e.g. example.com/s1. This tells Mailgun to sign the message with the signing domain example.com using the selector s1. Note: the domain key specified must have been previously created and activated.

o:secondary-dkim-public	
string
Specify an alias of the domain key specified in o:secondary-dkim. Also formatted as public_signing_domain/selector. o:secondary-dkim option must also be provided. Mailgun will sign the message with the provided key of the secondary DKIM, but use the public secondary DKIM name and selector. Note: We will perform a DNS check prior to signing the message to ensure the public keys matches the secondary DKIM.

o:deliverytime	
string
Specifies the scheduled delivery time in RFC-2822 format (https://documentation.mailgun.com/docs/mailgun/user-manual/get-started/#date-format). Depending on your plan, you can schedule messages up to 3 or 7 days in advance. If your domain has a custom message_ttl (time-to-live) setting, this value determines the maximum scheduling duration.

o:deliverytime-optimize-period	
string
Toggles Send Time Optimization (STO) on a per-message basis. String should be set to the number of hours in [0-9]+h format, with the minimum being 24h and the maximum being 72h. This value defines the time window in which Mailgun will run the optimization algorithm based on prior engagement data of a given recipient. See Sending a Message with STO for details. Please note that STO is only available on certain plans. See www.mailgun.com/pricing for more info

o:time-zone-localize	
string
Toggles Timezone Optimization (TZO) on a per message basis. String should be set to preferred delivery time in HH:mm or hh:mmaa format, where HH:mm is used for 24 hour format without AM/PM and hh:mmaa is used for 12 hour format with AM/PM. See Sending a Message with TZO for details. Please note that TZO is only available on certain plans. See www.mailgun.com/pricing for more info

o:testmode	
string
Enables sending in test mode. See Sending in Test Mode

Value	Description
yes	Send in test mode
o:tracking	
string
Toggles both click and open tracking on a per-message basis, see Tracking Messages for details.

Enum Value	Description
yes	Enable tracking on a per-message basis
no	Disable tracking on a per-message basis
true	Enable tracking on a per-message basis
false	Disable tracking on a per-message basis
htmlonly	Use if you only want links rewritten in the HTML part of the message
o:tracking-clicks	
string
Toggles click tracking on a per-message basis, see Tracking Clicks. Has higher priority than domain-level setting.

Enum Value	Description
yes	Enable tracking on a per-message basis
no	Disable tracking on a per-message basis
true	Enable tracking on a per-message basis
false	Disable tracking on a per-message basis
htmlonly	Use if you only want links rewritten in the HTML part of the message
o:tracking-opens	
string
Toggles opens tracking on a per-message basis, see Tracking Opens. Has higher priority than domain-level setting.

Enum Value	Description
yes	Enables opens tracking
no	Disable opens tracking
true	Enables opens tracking
false	Disable opens tracking
o:require-tls	
string
Requires the message only be sent over a TLS connection, see TLS Sending Connection Settings. If a TLS connection can not be established, Mailgun will not deliver the message. If set to false or no, Mailgun will still try and upgrade the connection, but if Mailgun cannot, the message will be delivered over a plaintext SMTP connection. The default is false

Enum Value	Description
yes	Message only be sent over a TLS connection
no	Message do not require to be sent over a TLS connection
true	Message only be sent over a TLS connection
false	Message do not require to be sent over a TLS connection
o:skip-verification	
string
If true, the certificate and hostname of the resolved MX Host will not be verified when trying to establish a TLS connection. If false, Mailgun will verify the certificate and hostname. If either one can not be verified, a TLS connection will not be established. The default is false

Enum Value	Description
yes	Verification skipped
no	Verification active
true	Verification skipped
false	Verification active
o:sending-ip	
string
Used to specify an IP Address to send an email that is owned by your account

o:sending-ip-pool	
string
If an IP Pool ID is provided, the email will be delivered with an IP that belongs in that pool

o:tracking-pixel-location-top	
string
If you send long emails that experience truncation or other rendering issues at the recipient, you can ensure opens are being tracked accurately with placement of the tracking pixel at the top of your emails

Enum Value	Description
yes	Enables tracking
no	Disable tracking
true	Enables tracking
false	Disable tracking
htmlonly	Use if you only want links rewritten in the HTML part of the message
h:X-My-Header	
string
h: prefix followed by a Header/Value pair. For example: h:X-Mailgun-Sending-Ip-Pool=xx.xx.xxx.x.

v:my-var	
string
v: prefix followed by an arbitrary name allows to attach a custom JSON data to the message. See Attaching Data to Messages for more information

recipient-variables	
string
A valid JSON-encoded dictionary, where key is a plain recipient address and value is a dictionary with variables that can be referenced in the message body. See Batch Sending for more information

property name*
additional property
any
Responses
200A 200 response
Response Schema: application/json
id
required
string
message
required
string
400A 400 response
401A 401 response
429A 429 response
500A 500 response
Request samples
curl
Go
Node.js
PHP
Java
Python

2 more
2 more
Copy
import FormData from 'form-data';
import fetch from 'node-fetch';

async function run() {
  const form = new FormData();
  form.append('from','string');
  form.append('to','string');
  form.append('subject','string');
  form.append('html','string');

  const domainName = 'YOUR_domain_name_PARAMETER';
  const resp = await fetch(
    `https://api.mailgun.net/v3/${domainName}/messages`,
    {
      method: 'POST',
      headers: {
        Authorization: 'Basic ' + Buffer.from('<username>:<password>').toString('base64')
      },
      body: form
    }
  );

  const data = await resp.text();
  console.log(data);
}

run();
Response samples
200
400
401
429
500
application/json

Example
Example
Copy
{
"id": "message-id",
"message": "Queued. Thank you."
}
Send an email in MIME format
post
/v3/{domain_name}/messages.mime
Build a MIME string yourself using a MIME library for your programming language and submit it to Mailgun.

Security
basicAuth
Request
path Parameters
domain_name
required
string
Domain name used to send the message

Request Body schema: multipart/form-data
required
to
required
Array of strings
Email address of the recipient(s). Example: "Bob <bob@host.com>". You can use commas to separate multiple recipients

message
required
string <binary>
MIME string of the message. Make sure to use multipart/form-data content type to send this as a file upload

template	
string
Name of a template stored via template API to use to render the email body. See Templates for more information

t:version	
string
Render a specific version of the given template instead of the latest version. o:template option must also be provided.

t:text	
string
Render template in the text part of the message in case of template sending

Value	Description
yes	Render template in the text part of the message
t:variables	
string
A valid JSON-encoded dictionary used as the input for template variable expansion. See Templates for more information

o:tag	
Array of strings
Tag string. See Tagging for more information

o:dkim	
string
Enables/disables DKIM signatures on a per-message basis

Enum Value	Description
yes	Enables DKIM signatures
no	Disable DKIM signatures
true	Enables DKIM signatures
false	Disable DKIM signatures
o:secondary-dkim	
string
Specify a second domain key to sign the email with. The value is formatted as signing_domain/selector, e.g. example.com/s1. This tells Mailgun to sign the message with the signing domain example.com using the selector s1. Note: the domain key specified must have been previously created and activated.

o:secondary-dkim-public	
string
Specify an alias of the domain key specified in o:secondary-dkim. Also formatted as public_signing_domain/selector. o:secondary-dkim option must also be provided. Mailgun will sign the message with the provided key of the secondary DKIM, but use the public secondary DKIM name and selector. Note: We will perform a DNS check prior to singing the message to ensure the public keys matches the secondary DKIM.

o:deliverytime	
string
Specifies the scheduled delivery time in RFC-2822 format (https://mailgun-docs.redoc.ly/docs/mailgun/api-reference/intro/#date-format). Depending on your plan, you can schedule messages up to 3 or 7 days in advance. If your domain has a custom message_ttl (time-to-live) setting, this value determines the maximum scheduling duration.

o:deliverytime-optimize-period	
string
Toggles Send Time Optimization (STO) on a per-message basis. String should be set to the number of hours in [0-9]+h format, with the minimum being 24h and the maximum being 72h. This value defines the time window in which Mailgun will run the optimization algorithm based on prior engagement data of a given recipient. See Sending a Message with STO for details. Please note that STO is only available on certain plans. See www.mailgun.com/pricing for more info

o:time-zone-localize	
string
Toggles Timezone Optimization (TZO) on a per message basis. String should be set to preferred delivery time in HH:mm or hh:mmaa format, where HH:mm is used for 24 hour format without AM/PM and hh:mmaa is used for 12 hour format with AM/PM. See Sending a Message with TZO for details. Please note that TZO is only available on certain plans. See www.mailgun.com/pricing for more info

o:testmode	
string
Enables sending in test mode. See Sending in Test Mode

Value	Description
yes	Send in test mode
o:tracking	
string
Toggles both click and open tracking on a per-message basis, see Tracking Messages for details.

Enum Value	Description
yes	Enable tracking on a per-message basis
no	Disable tracking on a per-message basis
true	Enable tracking on a per-message basis
false	Disable tracking on a per-message basis
htmlonly	Use if you only want links rewritten in the HTML part of the message
o:tracking-clicks	
string
Toggles click tracking on a per-message basis, see Tracking Clicks. Has higher priority than domain-level setting.

Enum Value	Description
yes	Enable tracking on a per-message basis
no	Disable tracking on a per-message basis
true	Enable tracking on a per-message basis
false	Disable tracking on a per-message basis
htmlonly	Use if you only want links rewritten in the HTML part of the message
o:tracking-opens	
string
Toggles opens tracking on a per-message basis, see Tracking Opens. Has higher priority than domain-level setting.

Enum Value	Description
yes	Enables opens tracking
no	Disable opens tracking
true	Enables opens tracking
false	Disable opens tracking
o:require-tls	
string
Requires the message only be sent over a TLS connection, see TLS Sending Connection Settings. If a TLS connection can not be established, Mailgun will not deliver the message. If set to false or no, Mailgun will still try and upgrade the connection, but if Mailgun cannot, the message will be delivered over a plaintext SMTP connection. The default is false

Enum Value	Description
yes	Message only be sent over a TLS connection
no	Message do not require to be sent over a TLS connection
true	Message only be sent over a TLS connection
false	Message do not require to be sent over a TLS connection
o:skip-verification	
string
If true, the certificate and hostname of the resolved MX Host will not be verified when trying to establish a TLS connection. If false, Mailgun will verify the certificate and hostname. If either one can not be verified, a TLS connection will not be established. The default is false

Enum Value	Description
yes	Verification skipped
no	Verification active
true	Verification skipped
false	Verification active
o:sending-ip	
string
Used to specify an IP Address to send an email that is owned by your account

o:sending-ip-pool	
string
If an IP Pool ID is provided, the email will be delivered with an IP that belongs in that pool

o:tracking-pixel-location-top	
string
If you send long emails that experience truncation or other rendering issues at the recipient, you can ensure opens are being tracked accurately with placement of the tracking pixel at the top of your emails

Enum Value	Description
yes	Enables tracking
no	Disable tracking
true	Enables tracking
false	Disable tracking
htmlonly	Use if you only want links rewritten in the HTML part of the message
h:X-My-Header	
string
h: prefix followed by a Header/Value pair. For example: h:X-Mailgun-Sending-Ip-Pool=xx.xx.xxx.x.

v:my-var	
string
v: prefix followed by an arbitrary name allows to attach a custom JSON data to the message. See Attaching Data to Messages for more information

recipient-variables	
string
A valid JSON-encoded dictionary, where key is a plain recipient address and value is a dictionary with variables that can be referenced in the message body. See Batch Sending for more information

property name*
additional property
any
Responses
200A 200 response
Response Schema: application/json
id
required
string
message
required
string
400A 400 response
401A 401 response
429A 429 response
500A 500 response
Request samples
curl
Go
Node.js
PHP
Java
Python

2 more
2 more
Copy
import FormData from 'form-data';
import fetch from 'node-fetch';

async function run() {
  const form = new FormData();
  form.append('to','string');
  form.append('message','string');

  const domainName = 'YOUR_domain_name_PARAMETER';
  const resp = await fetch(
    `https://api.mailgun.net/v3/${domainName}/messages.mime`,
    {
      method: 'POST',
      headers: {
        Authorization: 'Basic ' + Buffer.from('<username>:<password>').toString('base64')
      },
      body: form
    }
  );

  const data = await resp.text();
  console.log(data);
}

run();
Response samples
200
400
401
429
500
application/json

Example
Example
Copy
{
"id": "message-id",
"message": "Queued. Thank you."
}
Retrieve a stored email
get
/v3/domains/{domain_name}/messages/{storage_key}
Event(s) created from sending an email with Mailgun will contain a storage.key to use to retrieve the email.

Security
basicAuth
Request
path Parameters
domain_name
required
string
Domain name that was used to send the email

storage_key
required
string
Storage key from the emails associated events

Responses
200A 200 response
Response Schema: application/json
Content-Transfer-Encoding
required
string
Content-Type
required
string
From
required
string
Message-Id
required
string
Mime-Version
required
string
Subject
required
string
To
required
string
X-Mailgun-Tag
required
string
sender
required
string
recipients
required
string
from
required
string
subject
required
string
body-html
required
string
body-plain
required
string
stripped-html
required
string
stripped-text
required
string
stripped-signature
required
string
message-headers
required
Array of strings
X-Mailgun-Template-Name
required
string
X-Mailgun-Template-Variables
required
string
400A 400 response
404A 404 response
Request samples
curl
Go
Node.js
PHP
Java
Python

2 more
2 more
Copy
import fetch from 'node-fetch';

async function run() {
  const domainName = 'YOUR_domain_name_PARAMETER';
  const storageKey = 'YOUR_storage_key_PARAMETER';
  const resp = await fetch(
    `https://api.mailgun.net/v3/domains/${domainName}/messages/${storageKey}`,
    {
      method: 'GET',
      headers: {
        Authorization: 'Basic ' + Buffer.from('<username>:<password>').toString('base64')
      }
    }
  );

  const data = await resp.text();
  console.log(data);
}

run();
Response samples
200
400
404
application/json

Example
Example
CopyExpand allCollapse all
{
"Content-Transfer-Encoding": "7bit",
"Content-Type": "text/html; charset=ascii",
"From": "foo.bar@my-domain.com",
"Message-Id": "<xxxxxxxxxxxxx.111111111111111@my-domain.com>",
"Mime-Version": "1.0",
"Subject": "\"Mailgun is awesome\"",
"To": "cool.barr@cool.com, bar.baz@gmail.com",
"X-Mailgun-Tag": "Earth",
"sender": "foo.bar@my-domain.com",
"recipients": "cool.barr@cool.com, bar.baz@gmail.com",
"from": "foo.bar@my-domain.com",
"subject": "\"Mailgun is awesome\"",
"body-html": "<html>This is some html</html>",
"body-plain": "This is some html",
"stripped-html": "<html>This is some html</html>",
"stripped-text": "This is some html",
"stripped-signature": "the signature block stripped from the plain text message (if found)",
"message-headers": [
[
"Mime-Version",
"1.0"
],
[
"Subject",
"\"Mailgun is awesome\""
],
[
"From",
"foo.bar@my-domain.com"
],
[
"To",
"cool.barr@cool.com, bar.baz@gmail.com"
],
[
"X-Mailgun-Tag",
"Earth"
],
[
"Message-Id",
"<xxxxxxxxxxxxx.111111111111111@my-domain.com>"
],
[
"Content-Transfer-Encoding",
"7bit"
],
[
"Content-Type",
"text/html; charset=ascii"
]
],
"X-Mailgun-Template-Name": "my-awesome-template",
"X-Mailgun-Template-Variables": "{\"name\":\"Foo\",\"phrase\":\"Bar\"}"
}
Get messages queue status
get
/v3/domains/{name}/sending_queues
Provides default and scheduled message queue information.

Security
basicAuth
Request
path Parameters
name
required
string
The name of the domain you want get sending queues from

Responses
200A 200 response
Response Schema: application/json
regular
required
object
scheduled
required
object
401A 401 response
404A 404 response
Request samples
curl
Go
Node.js
PHP
Java
Python

2 more
2 more
Copy
import fetch from 'node-fetch';

async function run() {
  const name = 'YOUR_name_PARAMETER';
  const resp = await fetch(
    `https://api.mailgun.net/v3/domains/${name}/sending_queues`,
    {
      method: 'GET',
      headers: {
        Authorization: 'Basic ' + Buffer.from('<username>:<password>').toString('base64')
      }
    }
  );

  const data = await resp.text();
  console.log(data);
}

run();
Response samples
200
401
404
application/json

Example
Example
CopyExpand allCollapse all
{
"regular": {
"is_disabled": true,
"disabled": {
"until": "Mon, 02 Jan 2006 15:04:05 MST",
"reason": "You have too many messages in queue"
}
},
"scheduled": {
"is_disabled": true,
"disabled": {
"until": "Mon, 02 Jan 2006 15:04:05 MST",
"reason": "You have too many messages in queue"
}
}
}
Delete scheduled and undelivered mail
delete
/v3/{domain_name}/envelopes
Deletes all scheduled and undelivered mail from the domain queue. This endpoint must be called on the storage API host and in the domain's region. e.g. https://storage-us-east4.api.mailgun.net/v3/example.com/envelopes

The storage hosts are storage-us-east4.api.mailgun.net, storage-us-west1.api.mailgun.net, and storage-europe-west1.api.mailgun.net.

Security
basicAuth
Request
path Parameters
domain_name
required
string
The name of the domain you want to delete envelope from

Responses
200A 200 response
Response Schema: application/json
message
required
string
401A 401 response
404A 404 response
Request samples
curl
Go
Node.js
PHP
Java
Python

2 more
2 more
Copy
import fetch from 'node-fetch';

async function run() {
  const domainName = 'YOUR_domain_name_PARAMETER';
  const resp = await fetch(
    `https://api.mailgun.net/v3/${domainName}/envelopes`,
    {
      method: 'DELETE',
      headers: {
        Authorization: 'Basic ' + Buffer.from('<username>:<password>').toString('base64')
      }
    }
  );

  const data = await resp.text();
  console.log(data);
}

run();
Response samples
200
401
404
application/json

Example
Example
Copy
{
"message": "done"
}