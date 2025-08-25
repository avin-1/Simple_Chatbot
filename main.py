import streamlit as st
import langchain_helper as lch

st.title("Simple Chat Application")

if "history" not in st.session_state:
    st.session_state.history = []

temperature = st.slider("Creativity (temperature)", 0.0, 1.0, 0.7)

prompt = st.chat_input("Enter your message...")

if prompt:
    try:
        with st.spinner("Generating response..."):
            response = lch.chat(prompt, temperature=temperature)
    except Exception as e:
        response = f"Error: {str(e)}"

    st.session_state.history.append({"role": "user", "content": prompt})
    st.session_state.history.append({"role": "bot", "content": response})

for msg in st.session_state.history:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])
