# import neccessary library
import streamlit as st
import pandas as pd


df1 = pd.DataFrame({"Cats": ["Lion", "Tiger", "Leopard"],
                    "Raptors": ["Eagle", "Falcon", "Hawk"],
                    "Snakes": ["Viper", "Anaconda", "Python"]})

df2 = pd.DataFrame({"Cats": ["Jaguar", "Panther"],
                    "Raptors": ["Osprey", "Kite"],
                    "Snakes": ["Cobra", "Boomslang"]})

st.dataframe(df1)
st.dataframe(df2)

df = st.dataframe(df1)
df.add_rows(df2)


df3 = pd.DataFrame({"Cats": [3, 2, 5],
                    "Raptors": [6, 5, 1],
                    "Snakes)": [4, 5, 7]})

df4 = pd.DataFrame({"Cats": [7, 9],
                    "Raptors": [2, 6],
                    "Snakes)": [3, 4]})

st.line_chart(df3)
st.line_chart(df4)

chart = st.line_chart(df3)
chart.add_rows(df4)
