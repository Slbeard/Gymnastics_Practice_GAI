import streamlit as st
import requests
import json

# OpenAI API Key (Keep it secure)
API_KEY = "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"
HEADERS = {
    "Authorization": f"Bearer {API_KEY}"}

# Replace with your fine-tuned model ID
FINE_TUNED_MODEL = "ft:gpt-3.5-turbo-0125:personal::B6kk1I2j"

st.title("Fine-Tuned GPT Chatbot 🤖")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state["messages"] = []

# Display chat history
for msg in st.session_state["messages"]:
    role = "🤖" if msg["role"] == "assistant" else "🧑"
    st.markdown(f"**{role}:** {msg['content']}")

# User input
user_input = st.text_input("You:", "")

if st.button("Send") and user_input:
    # Append user input to chat history
    st.session_state["messages"].append({"role": "user", "content": user_input})

    # Call OpenAI API
    response = requests.post(
        "https://api.openai.com/v1/chat/completions",
        headers=HEADERS,
        json={
            "model": gpt-3.5-turbo-0125,
            "messages": st.session_state["messages"]
        }
    )

    # Process response
    if response.status_code == 200:
        assistant_reply = response.json()["choices"][0]["message"]["content"]
        st.session_state["messages"].append({"role": "assistant", "content": assistant_reply})
        st.experimental_rerun()
    else:
        st.error("Error communicating with OpenAI API. Check your API key and model ID.")
