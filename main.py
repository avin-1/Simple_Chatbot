import streamlit as st
import langchain_helper as lch
st.title("Simple Chat Application")

if "history" not in st.session_state:
    st.session_state.history = []

prompt = st.chat_input("Enter your message...")

if prompt:
    with st.spinner("Generating response..."):
        response = lch.chat(prompt)
    st.session_state.history.append({"role": "user", "content": prompt})
    st.session_state.history.append({"role": "bot", "content": response})

# Display history
for msg in st.session_state.history:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])
