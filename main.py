import langchain_helper as lch
import streamlit as st

st.title("Simple Chat Application")

prompt = st.text_area("enter Prompt")
bt = st.button("enter")

if bt :
    response = lch.chat(prompt)
    st.subheader("Answer: ")
    st.markdown(response)
