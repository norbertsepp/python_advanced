import streamlit as st 

# A HIBÁS MEGOLDÁS - tulajdonképp nem hibás, csak nem működik, mert minden klikkre újrakezdi
# 
# counter = 0
# st.write("Counter: ", counter)

# btn1 = st.button("Click me to count up")
# if btn1:
#     counter += 1
st.title("Session state demo (singleton pattern)")

if "counter" not in st.session_state:
    st.session_state["counter"] = 0

st.write("Counter before click: ", st.session_state["counter"])

if st.button("Count up"):
    st.session_state["counter"] += 1
    
st.write("Counter after click: ", st.session_state["counter"])
