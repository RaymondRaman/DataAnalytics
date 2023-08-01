import streamlit as st

# The title
st.title("Exploring Streamlit")

# Headings
st.header("Introduction")
st.subheader("Installation")
st.text("Learn how to install Streamlit")
st.markdown("Install Streamlit using `pip install streamlit`")
st.write("Once installed, run Streamlit using the command `streamlit hello`")

# Mathematical equations
st.latex(r"s \left ( t \right) = ut + \dfrac{1}{2} at^2")

#  caption
st.caption("Streamlit text options")
