import os
import json
import openai

from dotenv import load_dotenv
from tools import get_appointments, read_knowledgebase, send_email

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")


def load_incoming_emails(file_path='customer_req/incoming_emails.json'):
    """
    Loads incoming emails from a JSON file and returns the entire JSON object
    containing 'emails' (a list of email objects) and 'last_processed_id'.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)


def save_incoming_emails(data, file_path='customer_req/incoming_emails.json'):
    """
    Saves the updated emails data back to file, including 'last_processed_id'.
    """
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4)


def create_handling_plan(intent):
    """
    Calls OpenAI to create a step-by-step plan based on the customer's intent.
    """
    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[
            {
                "role": "developer",
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
    # Return the plan text as given by the model
    return response.choices[0].message.content


def parse_plan_and_execute(plan):
    """
    A simple example of parsing the plan for which tools to call.
    This is simplistic: in a real system, you'd parse the text carefully or
    use GPT function calling for more reliable tool invocation.

    We'll collect tool results in a dictionary and return them.
    """
    tool_results = {}

    # Check if plan references the knowledgebase
    if "read_knowledgebase" in plan.lower():
        kb_info = read_knowledgebase({"keyword": ""})
        # Truncate for demonstration
        tool_results["knowledgebase"] = kb_info[:200] + "..."

    # Check if plan references appointments
    if "appointments" in plan.lower():
        # Suppose the user wants the next day's appointments for demonstration
        appointments_data = get_appointments({"date": "2024-12-11"})
        tool_results["appointments"] = appointments_data

    return tool_results


def get_intent_and_extract_structured_data(email_body):
    """
    Calls OpenAI to:
      - Identify the user's intent
      - Extract relevant data (e.g., email, date)
      - Return structured JSON data
    """
    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are an AI assistant that determines the intent of customer emails and "
                    "extracts necessary information (email address, date, etc.). "
                    "Respond in valid JSON conforming to the schema."
                )
            },
            {
                "role": "user",
                "content": email_body
            }
        ],
        response_format={
            "type": "json_schema",
            "json_schema": {
                "name": "email_extract",
                "schema": {
                    "type": "object",
                    "properties": {
                        "email": {"type": "string"},
                        "date": {"type": "string"},
                        "intent": {"type": "string"}
                    },
                    "required": ["email", "intent"],
                    "additionalProperties": False
                }
            }
        }
    )

    # The model's output should be valid JSON
    return json.loads(response.choices[0].message.content)


def finalize_response(intent, tool_results):
    """
    Creates a final user-facing response by summarizing the context from tools
    and the intent, with OpenAI.
    """
    system_prompt = (
        "You are responding to a customer's request. You have the user's intent and any extra data from tools. "
        "Provide a concise, friendly response suitable for an email body."
    )
    user_content = (
        f"Intent: {intent}\n\n"
        f"Tool Results:\n{json.dumps(tool_results, indent=2)}"
    )

    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_content}
        ]
    )
    return response.choices[0].message.content


def save_structured_data_to_file(structured_data, file_path='src/data/data.json'):
    """
    Saves or appends structured data to data.json
    """
    # We assume the file already has {"structured_data": []}
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except FileNotFoundError:
        data = {"structured_data": []}

    data["structured_data"].append(structured_data)

    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)


def process_email(email):
    """
    Process a single email object:
      - Extract data using GPT
      - Save the data
      - Create a plan
      - Execute needed tools
      - Finalize a response
      - Send email back to user
    """
    email_body = email.get("body", "")
    extracted_info = get_intent_and_extract_structured_data(email_body)

    # Save extracted data to data.json
    save_structured_data_to_file(extracted_info)

    # Generate plan
    plan = create_handling_plan(extracted_info.get("intent", ""))
    # Run any needed tools based on the plan
    tool_results = parse_plan_and_execute(plan)

    # Craft final response
    final_text = finalize_response(extracted_info.get("intent", ""), tool_results)

    # Send the final answer back to the customer
    send_email({
        "to": extracted_info.get("email", "customer@example.com"),
        "subject": "Re: Your Inquiry",
        "html_content": f"<p>{final_text}</p>",
        "text_content": final_text
    })


def main():
    data = load_incoming_emails()

    emails = data.get("emails", [])
    last_processed_id = data.get("last_processed_id", 0)

    # Find new emails by checking ID
    new_emails = [mail for mail in emails if mail["id"] > last_processed_id]

    # Sort them by ID to process in ascending order
    new_emails.sort(key=lambda x: x["id"])

    for mail in new_emails:
        process_email(mail)
        # Update last_processed_id
        last_processed_id = max(last_processed_id, mail["id"])

    # Write the updated last_processed_id back
    data["last_processed_id"] = last_processed_id
    save_incoming_emails(data)


if __name__ == "__main__":
    main() 