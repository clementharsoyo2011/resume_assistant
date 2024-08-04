import streamlit as st
import time
import openai
from langchain.chat_models import ChatOpenAI
# from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain
from streamlit_pdf_viewer import pdf_viewer

# st.write("OPENAI_API_KEY", st.secrets["OPENAI_API_KEY"])

openai_client = openai.Client(api_key=st.secrets["OPENAI_API_KEY"])

assistant = openai_client.beta.assistants.retrieve("asst_EkXIj0Z0Kbq3KMIt5gYPkpyN")

st.set_page_config(page_title="AskClemmy", page_icon=":speech_baloon:", layout="wide")
st.title("🚀 Welcome to Clement's Page!")
col1, col2 = st.columns(2)

with col1:
    pdf_viewer("/Users/clementharsoyo/Desktop/personal_resume_chatbot/Clement_Harsoyo_Resume.pdf")
    with open("/Users/clementharsoyo/Desktop/personal_resume_chatbot/Clement_Harsoyo_Resume.pdf", "rb") as pdf_file:
        PDFbyte = pdf_file.read()
    st.download_button(
        label="Download Clement's Resume",
        data=PDFbyte,
        file_name="Clement_Harsoyo_Resume.pdf",
    )

with col2:
    if "thread_id" not in st.session_state and "messages" not in st.session_state:
        st.session_state.messages = []
        st.session_state.messages.append({"role": "assistant", "content": "Hi there! What would you like to know more about Clement?"})
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
            st.session_state.messages.append({"role": "assistant", "content": response.content[0].text.value})
            with st.chat_message("assistant"):
                st.markdown(response.content[0].text.value)