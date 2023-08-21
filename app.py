import streamlit as st

with st.sidebar:
    st.title('🤖💬 OpenAI Chatbot :flag-in:')
    api_key = st.text_input('Enter OpenAI API token:', type='password')
    if not (api_key.startswith('sk-') and len(api_key)==51):
            st.warning('Please enter your credentials!', icon='⚠️')
        else:
            st.success('Proceed to entering your prompt message!', icon='👉')

