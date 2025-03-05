import streamlit as st
import openai

openai.api_key = st.secrets["OPENAI_API_KEY"]

FINE_TUNED_MODEL = "ft:gpt-3.5-turbo-0125:personal::B6kk1I2j"

if 'messages' not in st.session_state:
    st.session_state['messages'] = []

st.set_page_config(page_title="Gymnastics Practice Generator")

with st.sidebar:
    st.markdown("""
    # About \n
    Provide the duration and level of your class to generate a practice plan.\n
    You can also specify which events you want to work on.
    """)

for message in st.session_state['messages']:
    with st.chat_message(message['role']):
        st.markdown(message['content'])

if prompt := st.chat_input("Enter your class details."):
    st.session_state['messages'].append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message('assistant'):
        full_response = ""
        message_placeholder = st.empty()
        stream = openai.chat.completions.create(
            model=FINE_TUNED_MODEL,
            messages=[
                {"role": message["role"], "content": message["content"]} for message in st.session_state['messages']
            ],
            temperature=0,
            max_tokens=3000,
            stream=True
        )

        for chunk in stream:
            if chunk.choices[0].delta.content is not None:
                full_response += chunk.choices[0].delta.content
                message_placeholder.markdown(full_response + "▌")
        message_placeholder.markdown(full_response)

        # Attempt to convert Markdown table to DataFrame
        try:
            # Simple regex to extract table data (this might need adjustment)
            rows = re.findall(r'\|(.*?)(\|)', full_response)
            data = [row[0].split('|') for row in rows]
            df = pd.DataFrame(data[1:], columns=data[0])  # assumes first row is header
            st.dataframe(df)
        except Exception as e:
            # If DataFrame conversion fails, display as Markdown
            st.markdown(full_response)
            print(f"Error converting to dataframe: {e}")

    st.session_state['messages'].append({"role": "assistant", "content": full_response})