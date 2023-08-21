import os
import openai
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
import streamlit as st
st.title('Langchain App')
st.header('A Langchain app _by_ :blue[Pratyush Ranjan Mishra] :sunglasses:')


if "messages" not in st.session_state:
    st.session_state.messages = []
    
with st.sidebar:
    st.title('🤖💬 OpenAI Chatbot :flag-in:')
    if 'OPENAI_API_KEY' in st.secrets:
        st.success('API key already provided!', icon='✅')
        openai.api_key = st.secrets['OPENAI_API_KEY']
        llm = OpenAI(openai_api_key=st.secrets['OPENAI_API_KEY'])
    else:
        openai.api_key = st.text_input('Enter OpenAI API token:', type='password')
        if not (openai.api_key.startswith('sk-') and len(openai.api_key)==51):
            st.warning('Please enter your credentials!', icon='⚠️')
        else:
            st.success('Proceed to entering your prompt message!', icon='👉')


if prompt := st.chat_input("What is up?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
    st.session_state.messages.append({"role": "assistant", "content": full_response})
