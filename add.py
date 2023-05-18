import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt # !pip install matplotlib

st.title("map")
df = pd.DataFrame(np.random.randn(500, 2) / [50, 50] + [37.36, -122.4], columns=['lat', 'lon'])
st.map(df)
# x = st.slider('Select a value')
# st.write(x, ' squared is ', x * x)

rand = np.random.normal(1, 2, size=20)
fig, ax = plt.subplots()
ax.hist(rand, bins = 15)
st.pyplot(fig)
