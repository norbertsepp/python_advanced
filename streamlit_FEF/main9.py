#session state with key

import streamlit as st 
import time

sl = st.slider("Slider", 1, 20, 10, key="my_slider")

for i in range(20):
    st.session_state["my_slider"] = i
    time.sleep(0.2)
