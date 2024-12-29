from translator import translate_yoruba_to_target

def test_translation():
    # Test cases
    test_texts = [
        "How you dey?",
        "Wetin dey happen?",
        "I wan chop"
    ]
    
    target_language = "English"
    
    print("Testing Pidgin to English translations:\n")
    
    for text in test_texts:
        try:
            translation = translate_yoruba_to_target(text, target_language)
            print(f"Original: {text}")
            print(f"Translated: {translation}")
            print("-" * 50)
        except Exception as e:
            print(f"Error translating '{text}': {str(e)}")
            print("-" * 50)

if __name__ == "__main__":
    test_translation() 