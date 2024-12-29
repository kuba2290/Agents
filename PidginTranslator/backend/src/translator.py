import openai
from dotenv import load_dotenv

# ANSI escape codes for colors
NEON_GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"
BOLD = "\033[1m"

def translate_pidgin_to_target(text: str, target_language: str) -> str:
    """
    Translate Pidgin English text to the specified target language using OpenAI's GPT-4 model.

    Args:
        text: The Pidgin English text to translate.
        target_language: The target language for translation.

    Returns:
        str: The translated text or error message.
    """
    try:
        response = openai.chat.completions.create(
            model="gpt-4o",
            messages=[
                {
                    "role": "system",
                    "content": "You are a professional translator specializing in translating Pidgin English to other languages. Provide accurate and natural-sounding translations while preserving the original meaning and context."
                },
                {
                    "role": "user",
                    "content": f"Translate the following text to {target_language}. Maintain the tone and context:\n\n{text}"
                }
            ],
            temperature=0.3,
            max_tokens=500
        )
        
        return response.choices[0].message.content.strip()

    except openai.APIError as api_error:
        return f"OpenAI API error: {str(api_error)}"
    except Exception as e:
        return f"An unexpected error occurred: {str(e)}"

def main():
    # Simple command-line interface
    print(f"{BOLD}Pidgin Translator{RESET}")
    print("-----------------")
    while True:
        print(f"\nEnter text to translate (or 'q' to quit): {RED}", end="")
        text = input()
        print(RESET, end="")
        if text.lower() == 'q':
            break
            
        print(f"Enter target language: {RED}", end="")
        target = input()
        print(RESET, end="")
        try:
            translation = translate_pidgin_to_target(text, target)
            print(f"\nTranslation: {NEON_GREEN}{translation}{RESET}")
        except Exception as e:
            print(f"Error: {str(e)}")

if __name__ == "__main__":
    load_dotenv()  # Load environment variables
    main()