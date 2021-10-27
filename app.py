# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import streamlit as st
import pandas as pd
import numpy as np


header = st.container()
dataset= st.container()
features = st.container()
modelTraining = st.container()

with header:
    st.title("Welcome to my new web app")
    st.write('This is a table')
    dataframe = pd.DataFrame(np.random.randn(10, 20),
                             columns = ('col %d' % i
                                        for i in range(20)))
st.write(dataframe)
st.write('This is a line_chart.')
st.line_chart(dataframe)

