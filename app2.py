import streamlit as st
import requests

# Hugging Face API Details
API_URL = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.3"
HEADERS = {"Authorization": "Bearer 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"}

# Function to Query Hugging Face API
def medical_chatbot(question):
    payload = {"inputss": question}
    response = requests.post(API_URL, headers=HEADERS, json=payload)

    if response.status_code == 200:
        return response.json()[0]["generated_text"]
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
