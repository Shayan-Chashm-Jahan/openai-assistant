from dotenv import load_dotenv
import os
from openai import OpenAI

load_dotenv()

api_key = os.getenv('OPENAI_API_KEY')

if api_key:
    print("API Key loaded succesfully")
else:
    print("Failed to load API Key")

client = OpenAI(api_key=api_key)

messages = [
    {"role": "system", "content": "You are a helpful assistant."}, 
    {"role": "user", "content": "Hello, OPENAI!"}
]

try:
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages
    )

    print("API call successful")

    print(response.choices[0].message.content.strip())

except Exception as e:
    print(f"API call failed: {e}")