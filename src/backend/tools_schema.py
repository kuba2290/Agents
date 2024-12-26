"""
This file defines the schemas or parameters for the tools that the AI agent can call.

Example:
    get_appointments_schema = {
        "name": "get_appointments",
        "description": "Retrieve list of appointment dates/times",
        "parameters": {
            "type": "object",
            "properties": {
                "date": {
                    "type": "string",
                    "description": "Date for which we want to retrieve available appointments, format YYYY-MM-DD"
                }
            },
            "required": ["date"],
            "additionalProperties": False
        }
    }

You can add more tools with their schemas below.
"""

get_appointments_schema = {
    "name": "get_appointments",
    "description": "Retrieve list of appointment dates/times from schedule.json",
    "parameters": {
        "type": "object",
        "properties": {
            "date": {
                "type": "string",
                "description": "Date for which we want to retrieve available appointments, format YYYY-MM-DD"
            }
        },
        "required": ["date"],
        "additionalProperties": False
    }
}

read_knowledgebase_schema = {
    "name": "read_knowledgebase",
    "description": "Read data from company_secrets.md",
    "parameters": {
        "type": "object",
        "properties": {
            "keyword": {
                "type": "string",
                "description": "Any keyword or phrase to search within the knowledgebase; can be empty if not relevant"
            }
        },
        "required": ["keyword"],
        "additionalProperties": False
    }
}

send_email_schema = {
    "name": "send_email",
    "description": "Send an email to the customer",
    "parameters": {
        "type": "object",
        "properties": {
            "to": {
                "type": "string",
                "description": "The email address of the recipient"
            },
            "subject": {
                "type": "string",
                "description": "The subject of the email"
            },
            "html_content": {
                "type": "string",
                "description": "The HTML version of the email content"
            },
            "text_content": {
                "type": "string",
                "description": "The plain text version of the email"
            }
        },
        "required": ["to", "subject", "html_content", "text_content"],
        "additionalProperties": False
    }
}

# Add any additional tool schemas here as needed. 