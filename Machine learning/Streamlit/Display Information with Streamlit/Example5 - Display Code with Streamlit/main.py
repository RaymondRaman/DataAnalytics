# import neccessary library
import streamlit as st

st.markdown("## Display code without execution")
code = '''st.audio("https://bit.ly/rainaws3")'''
st.code(code, language='python')

st.markdown("## Display code with execution")
with st.echo():
    st.audio("https://bit.ly/rainaws3")
