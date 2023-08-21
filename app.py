import streamlit as st

st.write('Pratyush\'s Generative AI *World!* :sunglasses:')

st.markdown('Streamlit is **_really_ cool**.')
st.markdown("This text is :red[colored red], and this is **:blue[colored]** and bold.")
st.markdown(":red[$\sqrt{x^2+y^2}=1$] is a Pythagorean identity. :pencil:")

st.slider("This is a slider", 0, 100, (25, 75))
