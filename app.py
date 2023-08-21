import streamlit as st
import time
st.write('Pratyush\'s Generative AI *World!* :sunglasses:')

st.markdown('Streamlit is **_really_ cool**.')
st.markdown("This text is :red[colored red], and this is **:blue[colored]** and bold.")
st.markdown(":red[$\sqrt{x^2+y^2}=1$] is a Pythagorean identity. :pencil:")

age = st.slider('How old are you?', 0, 130, 25)
st.write("I'm ", age, 'years old')

title = st.text_input('Movie title', 'Life of Brian')
st.write('The current movie title is', title)

if prompt := st.chat_input("What is up?"):
  st.write(prompt)


with st.sidebar:
    with st.echo():
        st.write("This code will be printed to the sidebar.")

    with st.spinner("Loading..."):
        time.sleep(5)
    st.success("Done!")
