import streamlit as st
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI

with st.sidebar:
    st.title('🤖💬 OpenAI Chatbot :flag-in:')
    api_key = st.text_input('Enter OpenAI API token:', type='password')
    llm = OpenAI(openai_api_key=api_key)
    if not (api_key.startswith('sk-') and len(api_key)==51):
            st.warning('Please enter your credentials!', icon='⚠️')
    else:
            st.success('Proceed to entering your prompt message!', icon='👉')


chat_model = ChatOpenAI()

