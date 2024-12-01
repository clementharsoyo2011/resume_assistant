import streamlit as st
import openai
import re
import time
import os

openai_client = openai.Client(
    api_key=os.environ["OPENAI_API_KEY"],
    default_headers={"OpenAI-Beta": "assistants=v2"}
)

assistant = openai_client.beta.assistants.retrieve("asst_EkXIj0Z0Kbq3KMIt5gYPkpyN")

def chat():
    if "thread_id" not in st.session_state and "messages" not in st.session_state:
            st.session_state.messages = []
            st.session_state.messages.append({"role": "assistant", "content": "Hi there! What would you like to know about Clement?"})
            thread = openai_client.beta.threads.create(
                messages = st.session_state.messages
            )
            st.session_state.thread_id = thread.id
            if "chat_history" not in st.session_state:
                st.session_state.chat_history = []

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
        
    if prompt := st.chat_input("Ask Something!"):
        with st.chat_message("user"):
            st.markdown(prompt)
        
        st.session_state.messages.append({"role": "user", "content": prompt})

        openai_client.beta.threads.messages.create(
            thread_id = st.session_state.thread_id,
            role = "user",
            content = prompt
        )

        run = openai_client.beta.threads.runs.create(
            thread_id = st.session_state.thread_id,
            assistant_id = assistant.id,
            instructions="You are Clement Harsoyo's personal assistant. Your goal is to help Clement secure interviews and job offers. Your audience is a talent recruiter."
        )

        with st.spinner("Asnwering your question..."):
            while run.status != "completed":
                time.sleep(1)
                run = openai_client.beta.threads.runs.retrieve(
                    thread_id = st.session_state.thread_id,
                    run_id = run.id
                )
        
        messages = openai_client.beta.threads.messages.list(
            thread_id = st.session_state.thread_id
        )
        
        assistant_responses = [message for message in messages if message.run_id == run.id and message.role == "assistant"]

        for response in assistant_responses:
            # Remove citation
            response_messages_processed = re.sub('【.*?†source】', '', response.content[0].text.value)
            st.session_state.messages.append({"role": "assistant", "content": response_messages_processed})
            with st.chat_message("assistant"):
                st.markdown(response_messages_processed)