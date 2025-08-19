import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv
import os


load_dotenv()
key = os.getenv("OPENAI_API_KEY")
st.title("Chatbot")

if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role":"assistant", "content":"how can i help you?"}]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

    if prompt := st.chat_input():
        if not key:
            st.info("add key now")
            st.stop()

        client = OpenAI(api_key=key)
        st.session_state.messages.append({"role":"user","content":prompt})
        st.chat_message("user").write(prompt)
        response = client.chat.completions.create(model="gpt-4o", messages=st.session_state.messages)
        msg = response.choices[0].message.content
        st.session_state.messages.append({"role":"assistant","content":msg})
        st.chat_message("assistant").write(msg)

