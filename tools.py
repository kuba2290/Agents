import json
import os

import requests
from dotenv import load_dotenv

# Load environment variables (Mailgun config, for example)
load_dotenv()
MAILGUN_API_KEY = os.getenv("MAILGUN_API_KEY", "")
MAILGUN_DOMAIN = os.getenv("MAILGUN_DOMAIN", "")
MAILGUN_API_URL = f"https://api.mailgun.net/v3/{MAILGUN_DOMAIN}/messages.mime"

def get_appointments(parameters: dict) -> dict:
    """
    Retrieve list of appointment times for a specified date from schedule.json.
    parameters: 
      {
        "date": "YYYY-MM-DD"
      }
    """
    date_str = parameters.get("date")
    schedule_file = os.path.join("src", "data", "schedule.json")
    with open(schedule_file, 'r') as file:
        schedule_data = json.load(file)

    appointments_for_date = [
        appt for appt in schedule_data["appointments"] if appt["date"] == date_str
    ]
    return {"appointments": appointments_for_date}

def read_knowledgebase(parameters: dict) -> str:
    """
    Read data from company_secrets.md. 
    Optionally search by keyword if given in 'parameters["keyword"]'.
    """
    keyword = parameters.get("keyword", "")
    kb_file = os.path.join("docs", "company_secrets.md")
    with open(kb_file, 'r', encoding='utf-8') as file:
        kb_data = file.read()

    if keyword:
        # In a real system, you might add logic to highlight or extract relevant sections
        # For now, let's just ensure the data is returned.
        pass

    return kb_data

def _create_mime_message(to: str, subject: str, html_content: str, text_content: str) -> str:
    """
    Builds a MIME multipart string for sending via Mailgun
    """
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText

    message = MIMEMultipart('alternative')
    message['From'] = f"support@{MAILGUN_DOMAIN}"
    message['To'] = to
    message['Subject'] = subject

    part1 = MIMEText(text_content, 'plain')
    part2 = MIMEText(html_content, 'html')
    message.attach(part1)
    message.attach(part2)

    return message.as_string()

def send_email(parameters: dict) -> dict:
    """
    Send an email via Mailgun using the messages.mime endpoint.
    parameters:
      {
        "to": "customer@example.com",
        "subject": "Subject text",
        "html_content": "<p>Hello</p>",
        "text_content": "Hello"
      }
    """
    to = parameters.get("to")
    subject = parameters.get("subject")
    html_content = parameters.get("html_content")
    text_content = parameters.get("text_content")

    if not MAILGUN_API_KEY or not MAILGUN_DOMAIN:
        return {"status": "error", "message": "Mailgun config missing"}

    mime_msg = _create_mime_message(to, subject, html_content, text_content)
    response = requests.post(
        MAILGUN_API_URL,
        auth=("api", MAILGUN_API_KEY),
        files={"message": ("message.mime", mime_msg, "application/octet-stream")},
        data={"to": to}
    )
    return response.json() 