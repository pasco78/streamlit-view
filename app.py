import streamlit as st

st.title("hello streamlit!")

st.write('# Youtube view')
st.write('## raw')

view=[100,150,300]
view

st.bar_chart(view)

import pandas as pd

sview= pd.Series(view)
sview