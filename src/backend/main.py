import os
import json
import openai
import logging
from datetime import datetime
from dotenv import load_dotenv
from tools import get_appointments, read_knowledgebase, send_email

# Configure logging
def setup_logging():
    """Configure logging with timestamp, level, and message"""
    log_directory = "logs"
    if not os.path.exists(log_directory):
        os.makedirs(log_directory)
    
    # Create a timestamp for the log file name
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    log_file = os.path.join(log_directory, f'agent_{timestamp}.log')
    
    # Configure logging format and settings
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(log_file),
            logging.StreamHandler()  # This will also print to console
        ]
    )
    
    logging.info("Logging initialized")

# Initialize environment and logging
load_dotenv()
setup_logging()
logger = logging.getLogger(__name__)

# Set OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")
if not openai.api_key:
    logger.error("OpenAI API key not found in environment variables")
    raise ValueError("OpenAI API key not found")

def load_incoming_emails(file_path='customer_req/incoming_emails.json'):
    """Loads incoming emails from a JSON file"""
    logger.info(f"Loading emails from {file_path}")
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            logger.debug(f"Loaded {len(data.get('emails', []))} emails")
            return data
    except FileNotFoundError:
        logger.error(f"Email file not found: {file_path}")
        raise
    except json.JSONDecodeError:
        logger.error(f"Invalid JSON in email file: {file_path}")
        raise

def save_incoming_emails(data, file_path='customer_req/incoming_emails.json'):
    """Saves the updated emails data back to file"""
    logger.info(f"Saving updated emails to {file_path}")
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4)
            logger.debug("Successfully saved emails data")
    except Exception as e:
        logger.error(f"Failed to save emails: {str(e)}")
        raise

def create_handling_plan(intent):
    """Creates a step-by-step plan based on customer intent"""
    logger.info(f"Creating handling plan for intent: {intent}")
    try:
        client = openai.OpenAI()
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are a helpful assistant that creates a step-by-step plan "
                        "to handle a customer's request. Include instructions on which "
                        "tools to call (e.g., read_knowledgebase, get_appointments, "
                        "send_email) if appropriate."
                    )
                },
                {
                    "role": "user",
                    "content": f"The intent of the user is: {intent}. Please create a plan."
                }
            ]
        )
        plan = response.choices[0].message.content
        logger.debug(f"Generated plan: {plan}")
        return plan
    except Exception as e:
        logger.error(f"Failed to create handling plan: {str(e)}")
        raise

def parse_plan_and_execute(plan):
    """Parses and executes the handling plan"""
    logger.info("Parsing and executing plan")
    logger.debug(f"Plan content: {plan}")
    tool_results = {}

    try:
        if "read_knowledgebase" in plan.lower():
            logger.debug("Executing knowledgebase tool")
            kb_info = read_knowledgebase({"keyword": ""})
            tool_results["knowledgebase"] = kb_info[:200] + "..."

        if "get_appointments" in plan.lower() or "check appointments" in plan.lower():
            logger.debug("Executing appointments tool")
            appointments_data = get_appointments({"date": "2024-12-11"})
            tool_results["appointments"] = appointments_data

        logger.info(f"Executed {len(tool_results)} tools successfully")
        if not tool_results:
            logger.warning("No tools were executed based on the plan")
        return tool_results
    except Exception as e:
        logger.error(f"Error executing plan: {str(e)}")
        raise

def get_intent_and_extract_structured_data(email_body):
    """Extracts intent and structured data from email"""
    logger.info("Extracting intent and structured data from email")
    try:
        client = openai.OpenAI()
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are an AI assistant that determines the intent of customer emails and "
                        "extracts necessary information (email address, date, etc.). "
                        "You must respond with a valid JSON object containing these fields:\n"
                        "- email (string, required)\n"
                        "- date (string, optional)\n"
                        "- intent (string, required)\n\n"
                        "Example: {\"email\": \"user@example.com\", \"intent\": \"Schedule Appointment\", \"date\": \"2024-01-01\"}"
                    )
                },
                {
                    "role": "user",
                    "content": email_body
                }
            ]
        )
        data = json.loads(response.choices[0].message.content)
        logger.debug(f"Extracted data: {data}")
        return data
    except Exception as e:
        logger.error(f"Failed to extract data from email: {str(e)}")
        raise

def save_structured_data_to_file(structured_data, file_path=r'D:\Agents\data.json'):
    """Saves structured data to file"""
    logger.info(f"Saving structured data to {file_path}")
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except FileNotFoundError:
        logger.warning(f"Data file not found, creating new one: {file_path}")
        data = {"structured_data": []}

    data["structured_data"].append(structured_data)

    try:
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4)
            logger.debug("Successfully saved structured data")
    except Exception as e:
        logger.error(f"Failed to save structured data: {str(e)}")
        raise

def process_email(email):
    """Process a single email"""
    logger.info(f"Processing email ID: {email.get('id')}")
    try:
        email_body = email.get("body", "")
        extracted_info = get_intent_and_extract_structured_data(email_body)
        save_structured_data_to_file(extracted_info)

        plan = create_handling_plan(extracted_info.get("intent", ""))
        tool_results = parse_plan_and_execute(plan)

        final_text = finalize_response(extracted_info.get("intent", ""), tool_results)

        send_email({
            "to": extracted_info.get("email", "customer@example.com"),
            "subject": "Re: Your Inquiry",
            "html_content": f"<p>{final_text}</p>",
            "text_content": final_text
        })
        logger.info(f"Successfully processed email ID: {email.get('id')}")
    except Exception as e:
        logger.error(f"Failed to process email ID {email.get('id')}: {str(e)}")
        raise

def finalize_response(intent, tool_results):
    """
    Creates a final user-facing response by summarizing the context from tools
    and the intent, with OpenAI.
    """
    client = openai.OpenAI()
    system_prompt = (
        "You are responding to a customer's request. You have the user's intent and any extra data from tools. "
        "Provide a concise, friendly response suitable for an email body."
    )
    user_content = (
        f"Intent: {intent}\n\n"
        f"Tool Results:\n{json.dumps(tool_results, indent=2)}"
    )

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_content}
        ]
    )
    return response.choices[0].message.content

def main():
    """Main execution function"""
    logger.info("Starting email processing")
    try:
        data = load_incoming_emails()
        emails = data.get("emails", [])
        last_processed_id = data.get("last_processed_id", 0)

        new_emails = [mail for mail in emails if mail["id"] > last_processed_id]
        logger.info(f"Found {len(new_emails)} new emails to process")

        new_emails.sort(key=lambda x: x["id"])
        
        for mail in new_emails:
            try:
                process_email(mail)
                last_processed_id = max(last_processed_id, mail["id"])
            except Exception as e:
                logger.error(f"Error processing email {mail['id']}: {str(e)}")
                continue

        data["last_processed_id"] = last_processed_id
        save_incoming_emails(data)
        logger.info("Email processing completed successfully")
    except Exception as e:
        logger.error(f"Fatal error in main execution: {str(e)}")
        raise

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        logger.critical(f"Application failed: {str(e)}")
        raise 