import streamlit as st
import requests
from config import HUGGINGFACE_API_KEY  # Import API key from config.py

# Hugging Face API Details
API_URL = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.3"
HEADERS = {"Authorization": f"Bearer {HUGGINGFACE_API_KEY}"}

# Function to Query Hugging Face API
def medical_chatbot(question):
    payload = {"inputs": question}  # Fixed "inputss" typo to "inputs"
    response = requests.post(API_URL, headers=HEADERS, json=payload)

    if response.status_code == 200:
        return response.json()[0].get("generated_text", "⚠️ No response generated.")
    else:
        return f"⚠️ API Error: {response.status_code}, {response.json()}"

# Streamlit UI
def main():
    st.title("🩺 AI Medical Assistant (Mistral-7B)")
    user_input = st.text_input("Ask a medical question:")

    if st.button("Ask"):
        if user_input:
            with st.spinner("Processing..."):
                response = medical_chatbot(user_input)
            st.write("💡 **Assistant:**", response)
        else:
            st.warning("Please enter a question!")

if __name__ == "__main__":
    main()
