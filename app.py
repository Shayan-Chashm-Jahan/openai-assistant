import os
from openai import OpenAI 
import streamlit as st
from dotenv import load_dotenv

load_dotenv()
api_key = st.secrets["OPENAI_API_KEY"]

client = OpenAI(api_key=api_key)

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

    #Streamlit UI

    st.title("Art Assistant")
    st.write("Welcome to the Movies&Songs AI Assistant.")

    if 'conversation_history' not in st.session_state:
        st.session_state.conversation_history = [
             {"role": "system", "content": "You are an assistant specializing in movies and songs. Only respond to queries related to movies and songs. Avoid any other topics."}
        ]

    user_input = st.text_input("You: ")

    if user_input:
        st.session_state.conversation_history.append({"role": "user", "content": user_input})
        response = generate_response(st.session_state.conversation_history)

        st.session_state.conversation_history.append({"role": "assistant", "content": response})
        
        st.write(f"Assistant: {response}")

        for message in st.session_state.conversation_history:
            if message['role'] == 'assistant':
                st.write(f"Assistant: {message['content']}")
            elif message['role'] == 'user':
                st.write(f"You: {message['content']}")
