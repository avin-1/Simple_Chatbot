import langchain_helper as lch
import streamlit as st

st.title("Simple Chat Application")

# Initialize chat history
if "history" not in st.session_state:
    st.session_state.history = []

# Input box
prompt = st.text_area("Enter Prompt")

# Button
if st.button("Enter"):
    with st.spinner("Generating response..."):
        response = lch.chat(prompt)
    # Save to history
    st.session_state.history.append({"user": prompt, "bot": response})

# Display chat history
for chat in st.session_state.history:
    st.markdown(f"**You:** {chat['user']}")
    st.markdown(f"**Bot:** {chat['bot']}")
