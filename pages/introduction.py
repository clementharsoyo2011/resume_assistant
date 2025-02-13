import streamlit as st

st.header("🚀 Hi There! I'm a Product Manager who loves to code")
st.markdown("Clement Harsoyo's here! Currently a Product Manager at [Splore](https://splore.com), crafting Generative AI solutions with a blend of deep technical expertise and strategic product thinking. NUS Computing graduate specialized in AI and ML, eager to drive innovation and solve business challenges in Product Management and Data Science roles.")
st.markdown('''
#### Technical Skills
| **Skills** | **Tools and Technologies** |
|  :---:    | :---: |
| Product Management  | User Research, Product Strategy, Feature Prioritization, Go-to-Market Execution  |
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
