import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
#from scipy.signal import hilbert, chirp 
import math
import cmath

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

def Klauder(T=6., f1=10., f2=40., length=0.512, dt=0.001):
    k = (f2 - f1)/T
    f0 = (f2 + f1)/2
    i = complex(0, 1)
    p = np.pi
    t = np.linspace(-length/2, (length-dt)/2, int(length/dt))
    #y = t**2

    a = np.exp(2*pi*i*f0*t)
    y = (a * np.sin(pi*k*t*(T - t)) / (pi*k*t)).real

    #y = p*f4**2 * (np.sinc(f4*t))**2/(f4-f3) - p*f3**2 * (np.sinc(f3*t))**2/(f4-f3) - \
    #    p*f2**2 * (np.sinc(f2*t))**2/(f2-f1) - p*f1**2 * (np.sinc(f1*t))**2/(f2-f1)

    #y = y / np.amax(abs(y))

    return t, y

st.title('Klauder wavelet')
st.text('This is a web app do display wavelets')

#st.subheader("f(t) = ...")
st.latex(r'''
    a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
    \sum_{k=0}^{n-1} ar^k =
    a \left(\frac{1-r^{n}}{1-r}\right)
    ''')
f1 = st.slider('Select terminal low frequency (Hz)', value=10., min_value=1., max_value=240.)
f2 = st.slider('Select terminal low frequency (Hz)', value=40., min_value=1., max_value=240.)

st.write(f1, " - ", f2)

#f1 = 5
#f2 = 10

t, y = Klauder(7, f1, f2, 0.512, 0.001)

chart_data = pd.DataFrame(
   {
       "t": t,
       "y": y
   }
)

st.line_chart(chart_data, x="t", y="y")
