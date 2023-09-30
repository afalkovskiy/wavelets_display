import streamlit as st

st.title('Seismic Wavelets')
st.subheader('Alex Falkovskiy')
url = "https://www.rmseismic.com/lasviewer.html"
st.write("RM Seismic Software [rmseismic.com](%s)" % url)
st.write('The purpose of this web app is to illustrate how basic seismic wavelets change with the change of parameters.')
st.write('It is based on a paper by Harold Ryan: Ricker, Ormsby; Klander, Bntterworth - A Choice of wavelets, publised in CSEG Recorder, September 1994.')
