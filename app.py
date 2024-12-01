import streamlit as st
from streamlit_navigation_bar import st_navbar
import pages as pg

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
pages=["Introduction", "Chat with Clement", "Experience", "Projects"]

st.set_page_config(page_title="AskClement!", page_icon=":speech_baloon:")

page = st_navbar(
    pages=pages,
    styles=styles,
    options={"show_menu": True, "show_sidebar": True, "hide_nav": False}
)

if page == "Introduction":
    pg.introduction()
elif page == "Chat with Clement":
    pg.chat()
elif page == "Experience":
    pg.experience()
elif page == "Projects":
    pg.projects()
