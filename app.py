import streamlit as st

styles = {
    "nav": {
        "background-color": "rgb(123, 209, 146)",
    },
    "div": {
        "max-width": "48rem",
    },
    "span": {
        "border-radius": "0.5rem",
        "color": "rgb(49, 51, 63)",
        "margin": "0 0.125rem",
        "padding": "0.4375rem 0.625rem",
    },
    "active": {
        "background-color": "rgba(255, 255, 255, 0.25)",
    },
    "hover": {
        "background-color": "rgba(255, 255, 255, 0.35)",
    },
}

st.set_page_config(page_title="AskClement!", page_icon="👨‍💻")

pages = [st.Page("pages/introduction.py", title="Introduction"), 
st.Page("pages/chat.py", title="Chat"), 
st.Page("pages/experience.py", title="Experiences"),
st.Page("pages/projects.py", title="Projects")]

page = st.navigation(pages)

page.run()
