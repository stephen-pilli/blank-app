import streamlit as st

st.title("Information Sheet")

st.markdown(
    open(f"Information_Sheet.md", "r").read()
)
