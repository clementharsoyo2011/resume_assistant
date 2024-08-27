import streamlit as st

def introduction():
    st.header("🚀 Hi There! I'm a Product Manager who codes")
    st.markdown("Clement Harsoyo's here! Currently a Product Manager at [Splore](https://splore.com), crafting Generative AI solutions with a blend of deep technical expertise and strategic product thinking. NUS Computing graduate specialized in AI and ML, eager to drive innovation and solve business challenges in Product Management and Data Science roles.")
    st.markdown('''
    #### Technical Skills
    | **Skills** | **Tools and Technologies** |
    |  :---:    | :---: |
    | Artificial Intelligence  | Generative AI, RAG, Agentic Workflow, Open AI, Langchain  |
    | Machine Learning | Neural Networks, Transformers, Natural Language, Computer Vision |
    | Data Analytics  | Python, R, SQL, Tableau  |
    | Project Management | Jira, Confluence, Git |
    ''')
    st.markdown(''' #### Education 
    - Graduated with Honors (Distinction) from NUS School of Computing
    - Majored in Business Analytics, with specialisation in Machine Learning and Financial Analytics
    - Relevant coursework: Artificial Intelligence, Machine Learning, Search Engine, Computer Networks, Information Technologies in Financial Services
    ''')
    st.markdown(''' #### Contact Me ''')
    with open("pages/Clement_Harsoyo_Resume.pdf", "rb") as pdf_file:
        PDFbyte = pdf_file.read()
        st.download_button(
            label=":male-technologist: Download Clement's Resume",
            data=PDFbyte,
            file_name="Clement_Harsoyo_Resume.pdf",
        )
    st.link_button(label=":globe_with_meridians: Connect with Clement in LinkedIn", url="https://linkedin.com/in/clementharsoyo")
    if st.button(label=":incoming_envelope: Send Clement a message"):
        with st.form('form'):
            viewer_email = st.text_input('Email')
            viewer_message = st.text_input('Message')
            c1, c2 = st.columns([1.7, 8.3])
            with c1:
                st.form_submit_button('Send')
            with c2:
                st.form_submit_button("Close")