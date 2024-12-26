import os
import json
import logging

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