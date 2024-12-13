import json
import random

def load_intents():
    with open('Chatbot/pattern.json') as file:
        data = json.load(file)
    return data['intents']

def get_response(intent_tag):
    for intent in intents:
        if intent['tag'] == intent_tag:
            return random.choice(intent['responses'])
    return "I'm sorry, I don't understand that."

def chat():
    print("Chatbot: Hello! How can I help you today?")
    while True:
        user_input = input("You: ").lower()
        if user_input == 'exit':
            print("Chatbot: Goodbye!")
            break

        response = None
        for intent in intents:
            for pattern in intent['patterns']:
                if pattern.lower() in user_input:
                    response = get_response(intent['tag'])
                    break
            if response:
                break

        print("Chatbot:", response)

if __name__ == "__main__":
    intents = load_intents()
    chat()
