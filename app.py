import os
from dotenv import load_dotenv
import openai
import langchain
import streamlit as st
st.title('Langchain App')
st.header('A Langchain app _by_ :blue[Pratyush Ranjan Mishra] :sunglasses:')

with st.sidebar:
    st.title('🤖💬 OpenAI Chatbot :flag-in:')
    if 'OPENAI_API_KEY' in st.secrets:
        st.success('API key already provided!', icon='✅')
        openai.api_key = st.secrets['OPENAI_API_KEY']
    else:
        openai.api_key = st.text_input('Enter OpenAI API token:', type='password')
        if not (openai.api_key.startswith('sk-') and len(openai.api_key)==51):
            st.warning('Please enter your credentials!', icon='⚠️')
        else:
            st.success('Proceed to entering your prompt message!', icon='👉')

load_dotenv()
openai.api_key = os.getenv(st.secrets['OPENAI_API_KEY'])

response = langchain.generate_text(prompt="What are the benefits of using LangChain?", model="openai/gpt-3")
print(response)

