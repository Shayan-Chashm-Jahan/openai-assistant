import os
from openai import OpenAI 
import streamlit as st
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv('OPENAI_API_KEY')

client = OpenAI(api_key=api_key)
conversation_history = [
        {"role": "system", "content": "You are an assistant specializing in movies and songs. Only respond to queries related to movies and songs. Avoid any other topics."}
    ]

def generate_response(conversation_history):
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=conversation_history,
            max_tokens=150,
            temperature=0.7,
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return str(e)
    
if __name__ == "__main__":
    print("Welcome to the OpenAI Assistant. Type 'exit' to end the conversation")

    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            break

        conversation_history.append({"role": "user", "content": user_input})
        response = generate_response(conversation_history)

        conversation_history.append({"role": "assistant", "content": response})
        print(f"Assistant: {response}")
