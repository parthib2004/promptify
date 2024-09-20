import os
import requests
import streamlit as st
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

API_URL = "https://api-inference.huggingface.co/models/EleutherAI/gpt-neo-1.3B"
HF_API_TOKEN = os.getenv("HF_API_TOKEN")  # Get token from environment variable

headers = {"Authorization": f"Bearer {HF_API_TOKEN}"}

def query_huggingface_api(prompt):
    payload = {
        "inputs": prompt,
        "parameters": {
            "max_length": 300,
            "temperature": 0.7,
            "top_p": 0.95,
            "num_return_sequences": 1
        }
    }
    response = requests.post(API_URL, headers=headers, json=payload)

    if response.status_code == 200:
        return response.json()[0]["generated_text"]
    else:
        return f"Error: {response.status_code}, {response.text}"

# Streamlit app layout
st.set_page_config(page_title="Promptify", page_icon="🤖")

# Header and subtitle
st.header("🤖 Promptify")
st.subheader("Code & Completion Assistan")

# Add an image or logo (optional)
# st.image("path_to_your_image.png", use_column_width=True)

# Input area and button in a single row
user_input = st.text_area("Enter your request:", height=200, placeholder="e.g., Write a Python program to reverse a string.")

# Button below the input area for better alignment
if st.button("Generate"):
    if user_input:
        with st.spinner("Generating..."):
            generated_code = query_huggingface_api(user_input)
            st.code(generated_code, language='java')
    else:
        st.error("Please enter a prompt!")

# Footer
st.markdown("---")
st.markdown("Created with ❤️ by [Parthib Sarkar](https://parthib.me/)")