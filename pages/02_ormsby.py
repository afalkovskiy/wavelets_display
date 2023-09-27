import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
#from scipy.signal import hilbert, chirp
import math

st.title('ORMSBY wavelet')
st.text('This is a web app do display wavelets')

st.subheader("f(t) = ...")
f = st.slider('Select frequency from [1, 240] Hz', value=60., min_value=1., max_value=240.)
st.write("Frequency f3 = ", f)

f1 = 5
f2 = 10
f3 = f
f4 = f+20.
t, y = ORMSBY(f1, f2, f3, f4, 0.512, 0.001)

chart_data = pd.DataFrame(
   {
       "t": t,
       "y": y
   }
)

st.line_chart(chart_data, x="t", y="y")
