import langchain_helper as lch
import streamlit as st

title =st.title("Simple Chat Application")
prompt = st.text_area("enter Prompt")
bt = st.button("enter")

if bt :
    with st.spinner("Generating response..."):
        response = lch.chat(prompt)
    st.subheader("Answer: ")
    st.markdown(response)
