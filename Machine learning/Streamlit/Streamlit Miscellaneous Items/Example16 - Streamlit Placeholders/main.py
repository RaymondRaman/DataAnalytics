# import neccessary library
import streamlit as st
import time

with st.empty():
    for seconds in range(5):
        st.markdown(f"### ⏳ {seconds} seconds have passed")
        time.sleep(1)
    st.markdown("###  ✔️ 5 seconds over!")

placeholder = st.empty()
# Replace the placeholder with some text:
placeholder.markdown("### Hello")
time.sleep(2)
placeholder.info("This replaces Hello")

placeholder = st.empty()

placeholder.line_chart({"data": [1, 5, 2, 6]})
time.sleep(2)
# Replace the chart with several elements:
with placeholder.container():
    st.markdown("### This is one element within the container")
    time.sleep(2)
    st.markdown("### This is a second one, soon to be folllowed by an image")
    time.sleep(2)
    st.image("https://bit.ly/edus3ha")
    time.sleep(10)
# Clear all those elementss:
placeholder.empty()
