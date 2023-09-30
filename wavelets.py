import streamlit as st

st.title('Seismic Wavelets')
st.subheader('Alex Falkovskiy')
url = "https://www.rmseismic.com"
st.write("RM Seismic Software [rmseismic.com](%s)" % url)
st.write('The purpose of this web app is to illustrate how basic seismic wavelets change with the change of parameters.')
st.write('It is based on a paper by Harold Ryan: Ricker, Ormsby; Klander, Bntterworth - A Choice of wavelets, publised in CSEG Recorder, September 1994.')
st.write('A list of wavelets you can display and vary parameters:')
st.write('**Ricker, Ormsby, Klauder** - use left side menu to select.')

url1 = "https://www.rmseismic.com/lasviewer.html"
st.write("More geophysical web apps: [link](%s)" % url1)
