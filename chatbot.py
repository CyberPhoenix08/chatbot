import os
import openai
from dotenv import load_dotenv

# Load the API key from the .env file
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Chat history
chat_history = []

def chat_with_gpt():
    print("Welcome to AI Chatbot (type 'exit' to quit)")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break

        # Add user message to history
        chat_history.append({"role": "user", "content": user_input})

        try:
            # Send conversation to GPT
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",  # You can also use gpt-4 if you have access
                messages=chat_history
            )
            reply = response['choices'][0]['message']['content'].strip()
            print("Bot:", reply)

            # Add assistant reply to history
            chat_history.append({"role": "assistant", "content": reply})

        except Exception as e:
            print("Error:", e)

if __name__ == "__main__":
    chat_with_gpt()
