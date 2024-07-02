import streamlit as st 

main_container = st.container()
main_container2 = st.container()

if "counter"  not in st.session_state:
    st.session_state.counter = 0
    

if main_container.button("Up"):
    st.session_state.counter += 1
    main_container2.write(st.session_state.counter)
if main_container.button("reset"):
    st.session_state.counter = 0

