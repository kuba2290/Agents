import os
import json
import logging
import requests

logger = logging.getLogger(__name__)

def get_appointments(parameters: dict) -> dict:
    """
    Retrieve list of appointment times for a specified date from schedule.json.
    parameters: 
      {
        "date": "YYYY-MM-DD"
      }
    """
    date_str = parameters.get("date")
    schedule_file = r"D:\Agents\schedule.json"
    
    logger.debug(f"Looking for schedule file at: {schedule_file}")
    logger.debug(f"File exists: {os.path.exists(schedule_file)}")
    
    # Create default data if file doesn't exist
    if not os.path.exists(schedule_file):
        logger.info("Schedule file not found, creating default data")
        default_data = {
            "appointments": [
                {
                    "date": date_str,
                    "time": "09:00",
                    "status": "available"
                },
                {
                    "date": date_str,
                    "time": "10:00",
                    "status": "available"
                }
            ]
        }
        try:
            with open(schedule_file, 'w') as file:
                json.dump(default_data, file, indent=4)
            logger.debug("Created new schedule file with default data")
            return default_data
        except Exception as e:
            logger.error(f"Failed to create schedule file: {str(e)}")
            raise

    try:
        with open(schedule_file, 'r') as file:
            content = file.read()
            logger.debug(f"Raw file content: {content}")
            schedule_data = json.loads(content)
            
        appointments_for_date = [
            appt for appt in schedule_data["appointments"] if appt["date"] == date_str
        ]
        logger.debug(f"Found {len(appointments_for_date)} appointments for date {date_str}")
        return {"appointments": appointments_for_date}
    except Exception as e:
        logger.error(f"Error reading or parsing schedule file: {str(e)}")
        raise 

def read_knowledgebase(parameters: dict) -> str:
    """
    Read data from company_secrets.md. 
    Optionally search by keyword if given in 'parameters["keyword"]'.
    """
    keyword = parameters.get("keyword", "")
    kb_file = r"D:\Agents\company_secrets.md"  # Updated path
    
    logger.debug(f"Looking for knowledgebase file at: {kb_file}")
    logger.debug(f"File exists: {os.path.exists(kb_file)}")
    
    try:
        with open(kb_file, 'r', encoding='utf-8') as file:
            kb_data = file.read()
            logger.info("Successfully read knowledgebase file")
            logger.debug(f"Knowledgebase content length: {len(kb_data)}")

        if keyword:
            logger.debug(f"Searching for keyword: {keyword}")
            # Add keyword search logic here if needed
            pass

        return kb_data

    except FileNotFoundError:
        logger.error(f"Knowledgebase file not found at: {kb_file}")
        raise
    except Exception as e:
        logger.error(f"Error reading knowledgebase: {str(e)}")
        raise 

def send_email(parameters: dict) -> dict:
    """Send an email via Mailgun"""
    logger.info("=" * 50)
    logger.info("SENDING EMAIL")
    logger.info(f"To: {parameters.get('to')}")
    logger.info(f"Subject: {parameters.get('subject')}")
    logger.info(f"Text content: {parameters.get('text_content')}")
    logger.info("=" * 50)
    
    MAILGUN_API_KEY = os.getenv("MAILGUN_API_KEY")
    MAILGUN_DOMAIN = os.getenv("MAILGUN_DOMAIN")
    
    if not MAILGUN_API_KEY or not MAILGUN_DOMAIN:
        logger.error("Mailgun configuration missing")
        logger.error(f"MAILGUN_API_KEY exists: {bool(MAILGUN_API_KEY)}")
        logger.error(f"MAILGUN_DOMAIN exists: {bool(MAILGUN_DOMAIN)}")
        return {"status": "error", "message": "Mailgun config missing"}

    try:
        logger.info("Attempting to send email via Mailgun")
        response = requests.post(
            f"https://api.mailgun.net/v3/{MAILGUN_DOMAIN}/messages",
            auth=("api", MAILGUN_API_KEY),
            data={
                "from": f"AI Assistant <mailgun@{MAILGUN_DOMAIN}>",
                "to": parameters.get("to"),
                "subject": parameters.get("subject"),
                "text": parameters.get("text_content"),
                "html": parameters.get("html_content")
            }
        )
        logger.info("Mailgun API Response:")
        logger.info("-" * 50)
        logger.info(f"Status Code: {response.status_code}")
        logger.info(f"Response: {response.text}")
        logger.info("-" * 50)
        
        return response.json()
    except Exception as e:
        logger.error(f"Failed to send email: {str(e)}")
        logger.error(f"Exception type: {type(e)}")
        logger.error("=" * 50)
        raise 