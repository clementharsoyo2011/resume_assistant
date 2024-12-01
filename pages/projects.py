import streamlit as st

def projects():
    st.markdown(''' ## AI Projects ''')
    st.subheader("Job Application AI Assistant (Beta)", divider="blue")
    st.write("Personalised AI assistant that tailors resume to the specific job application, seamlessly and accurately.")
    video_file = open("pages/Resume_Customised_Agent.mp4", "rb")
    video_bytes = video_file.read()
    st.video(video_bytes)
    st.subheader("Resume Chatbot", divider="blue")
    st.write("Smart chatbot with comprehensive knowledge on with Clement's background and experience, enabling natural conversation. See [Chat with Clement] on the navigation bar above. ")
    st.markdown(''' ## Data Science Projects ''')
    st.subheader("Financial Report Analyzer for NatWest Market", divider="blue")
    st.write("Built machine learning solution for ESG report analysis, utilizing natural language processing techniques to conduct a robust assessment on portfolio company's ESG strategy.")