# import neccessary library
import streamlit as st
import pandas as pd

file = st.file_uploader("Select a file to upload", type=["png", "jpg"])

if file is not None:
    st.image(file)

df = pd.DataFrame({"Mammal": ['Cat', 'Bat', 'Fox'], 'Number': [3, 1, 5]})

st.dataframe(df)

st.download_button("Download data", df.to_csv(
    index=False), file_name="data.csv")
