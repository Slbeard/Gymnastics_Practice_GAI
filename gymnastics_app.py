import streamlit as st
import requests
import json
import time

# OpenAI API Key (Set this securely)
API_KEY = "your_openai_api_key"
HEADERS = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

st.title("GPT Fine-Tuning Dashboard")

# Upload training file
uploaded_file = st.file_uploader("Upload JSONL Training File", type="jsonl")

if uploaded_file:
    st.write("File uploaded successfully!")

    # Save the uploaded file temporarily
    with open("temp_training_file.jsonl", "wb") as f:
        f.write(uploaded_file.getbuffer())

    # Upload to OpenAI
    st.write("Uploading to OpenAI...")
    upload_response = requests.post(
        "https://api.openai.com/v1/files",
        headers=HEADERS,
        files={"file": open("temp_training_file.jsonl", "rb")},
        data={"purpose": "fine-tune"}
    )

    if upload_response.status_code == 200:
        file_id = upload_response.json()["id"]
        st.success(f"File uploaded! File ID: {file_id}")

        # Fine-tune the model
        st.write("Starting fine-tuning...")
        fine_tune_data = {
            "training_file": file_id,
            "model": "gpt-3.5-turbo",
            "hyperparameters": {"n_epochs": 4}
        }
        fine_tune_response = requests.post(
            "https://api.openai.com/v1/fine_tuning/jobs",
            headers=HEADERS,
            json=fine_tune_data
        )

        if fine_tune_response.status_code == 200:
            fine_tune_job_id = fine_tune_response.json()["id"]
            st.success(f"Fine-tuning started! Job ID: {fine_tune_job_id}")

            # Poll for status updates
            st.write("Tracking job progress...")
            while True:
                job_status = requests.get(
                    f"https://api.openai.com/v1/fine_tuning/jobs/{fine_tune_job_id}",
                    headers=HEADERS
                ).json()

                st.write(f"Status: {job_status['status']}")
                
                if job_status["status"] in ["succeeded", "failed"]:
                    break
                
                time.sleep(10)  # Wait before checking again
            
            st.success("Fine-tuning complete!")
        else:
            st.error("Failed to start fine-tuning.")
    else:
        st.error("File upload failed!")


