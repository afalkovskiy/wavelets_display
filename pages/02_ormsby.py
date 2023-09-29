import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
#from scipy.signal import hilbert, chirp
import math

pi = math.pi

def ORMSBY(f1=5., f2=10., f3=40., f4=45., length=0.512, dt=0.001):
    p = np.pi
    t = np.linspace(-length/2, (length-dt)/2, int(length/dt))

    # y = p*p*f4**2 * (np.sinc(f4*t))**2/(p*f4-p*f3) - p*p*f3**2 * (np.sinc(f3*t))**2/(p*f4-p*f3) - \
    #     p*p*f2**2 * (np.sinc(f2*t))**2/(p*f2-p*f1) - p*p*f1**2 * (np.sinc(f1*t))**2/(p*f2-p*f1)
    y = p*f4**2 * (np.sinc(f4*t))**2/(f4-f3) - p*f3**2 * (np.sinc(f3*t))**2/(f4-f3) - \
        p*f2**2 * (np.sinc(f2*t))**2/(f2-f1) - p*f1**2 * (np.sinc(f1*t))**2/(f2-f1)

    y = y / np.amax(abs(y))

    return t, y

st.title('ORMSBY wavelet')
st.text('This is a web app do display wavelets')

st.subheader("f(t) = ...")
#f = st.slider('Select frequency from [1, 240] Hz', value=60., min_value=1., max_value=240.)
#st.write("Frequency f3 = ", f)

#f1 = 5
#f2 = 10
#f3 = 60
#f4 = 70.

f1 = st.slider('Select frequency f1 (Hz)', value=5., min_value=1., max_value=240.)
f2 = st.slider('Select frequency f2 (Hz)', value=10., min_value=f1, max_value=240.)
f3 = st.slider('Select frequency f3 (Hz)', value=60., min_value=f2, max_value=240.)
f4 = st.slider('Select frequency f4 (Hz)', value=70., min_value=f3, max_value=240.)
st.write(f1, " - ", f2, " - ", f3, " - ", f4)

t, y = ORMSBY(f1, f2, f3, f4, 0.512, 0.001)

chart_data = pd.DataFrame(
   {
       "t": t,
       "y": y
   }
)

st.line_chart(chart_data, x="t", y="y")
