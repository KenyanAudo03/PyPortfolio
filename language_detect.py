# from langdetect import detect_langs

# def detect_languages(text, confidence_threshold=0.5):
#     try:
#         langs = detect_langs(text)
#         detected_languages = []

#         for lang_info in langs:
#             if lang_info.prob >= confidence_threshold:
#                 detected_languages.append((lang_info.lang, lang_info.prob))

#         return detected_languages
#     except Exception as e:
#         print(f"Error during language detection: {e}")
#         return []

# # Example usage
# text_to_check = input("Enter the text: ")
# detected_languages = detect_languages(text_to_check)

# if detected_languages:
#     print("Detected languages:")
#     for lang, prob in detected_languages:
#         print(f"{lang}: {prob}")
# else:
#     print("Language detection failed.")


from googletrans import Translator

def translate_text(text, target_language='en'):
    try:
        translator = Translator()
        translated_text = translator.translate(text, dest=target_language).text
        return translated_text
    except Exception as e:
        print(f"Error during translation: {e}")
        return None

# Example usage
text_to_translate = input("Enter the text to translate: ")
target_language = input("Enter the target language code (e.g., 'fr' for French): ")

translated_text = translate_text(text_to_translate, target_language)

if translated_text is not None:
    print(f"Translated text: {translated_text}")
else:
    print("Translation failed.")
