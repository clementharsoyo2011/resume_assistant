import streamlit as st

st.markdown(''' ## AI Projects ''')
st.subheader("Job Application AI Assistant (Beta)", divider="blue")
st.write("Personalised AI agents built with Crew AI and Open AI, trained to fine-tune resume to fit specific job description, seamlessly and accurately.")
video_file = open("pages/Resume_Customised_Agent.mp4", "rb")
video_bytes = video_file.read()
st.video(video_bytes)
st.subheader("Resume Chatbot", divider="blue")
st.page_link("pages/chat.py", label="Chat with Clement :male-technologist:")
st.write("Smart AI assistant built with Open AI, trained with comprehensive knowledge on with Clement's background and experience")
st.markdown(''' ## Data Science Projects ''')
st.subheader("Financial Report Analyzer for NatWest Market", divider="blue")
st.write("Built machine learning solution for ESG report analysis, utilizing natural language processing techniques to conduct a robust assessment on portfolio company's ESG strategy.")