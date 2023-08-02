# import neccessary library
import streamlit as st

st.help(print)


def identity_cat(cat):
    """
    I identify cats from images
    """
    # Code to identify cats


st.help(identity_cat)

delta = None
step = 0.5

humidity = 75.0

raise_humidity = st.button("Raise humidity")
if raise_humidity:
    humidity += step
st.metric(f"The humidity is", humidity, delta)

if "temperature" not in st.session_state:
    st.session_state['temperature'] = 25.0

raise_temperature = st.button("Raise temperature")
if raise_temperature:
    st.session_state['temperature'] += step
    delta = step

lower_temperature = st.button("Lower temperature")
if lower_temperature:
    st.session_state['temperature'] -= step
    delta = step

st.metric(f"The temperature is:", st.session_state['temperature'], delta)
