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
    
def handle_user_input():
    user_input = st.session_state.user_input
    st.session_state.conversation_history.append({"role": "user", "content": user_input})
    response = generate_response(st.session_state.conversation_history)
    st.session_state.conversation_history.append({"role": "assistant", "content": response})
    st.session_state.user_input = ""

if __name__ == "__main__":

    #Streamlit UI

    st.title("🎬🎵 OpenAI Movie & Song Assistant")
    st.write("Welcome! Feel free to chat with the assistant! Keep in mind that the assistant only likes to discuss movies and songs. The assistant will not discuss anything else")

    # Use a sidebar for additional information or controls
    st.sidebar.header("About")
    st.sidebar.info("This assistant specializes in discussing movies and songs. Ask anything related to these topics!")

    if 'conversation_history' not in st.session_state:
        st.session_state.conversation_history = [
             {"role": "system", "content": "You are an assistant specializing in movies and songs. Only respond to queries related to movies and songs. Avoid any other topics."}
        ]

    st.text_input("You:", key="user_input", on_change=handle_user_input)
    submit_button = st.button("Send", on_click=handle_user_input)

    st.markdown("### Conversation History")
    for message in st.session_state.conversation_history:
        if message['role'] == 'assistant':
            st.markdown(f"**Assistant:** {message['content']}")
        elif message['role'] == 'user':
            st.markdown(f"**You:** {message['content']}")

    # Adding custom CSS
    st.markdown("""
    <style>
        .stTextInput {
            border: 2px solid #4CAF50;
            border-radius: 5px;
            padding: 10px;
        }
        .stButton button {
            background-color: #4CAF50;
            color: white;
            border: none;
            border-radius: 5px;
            padding: 10px 20px;
            text-align: center;
            display: inline-block;
            font-size: 16px;
        }
        .stMarkdown p {
            font-family: 'Arial', sans-serif;
            font-size: 14px;
        }
    </style>
    """, unsafe_allow_html=True)