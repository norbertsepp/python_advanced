import streamlit as st 
import time 
 
st.write("Hello, there, let's demonstrate streamlit through some widgets")

st.header("This is the Header element")
st.markdown("""# This is the Markdown-coded header
            > with some quotes
            - and list
            - items
            - in the text
            """)

st.code("""# Let's add some python code
        x = 2024
        y = str(x)
        print(x, ': -->', y)""")
st.latex(r"""LaTeX : 
         
         
         
         a+a r^1+a r^2+a r^3 
         """)

st.image("..\pythonlogo_l1.png", width=300)
#st.audio("Audio.mp3")
#st.video("video.mp4")
st.checkbox("This is a CHECKbox")

st.button('Click this button')
st.radio('Pick your gender using radio buttons',['Male','Female'])
st.selectbox('Pick your gender using a selectbox',['Male','Female'])
st.multiselect('Choose a planet with this multiselect widget',['Jupiter', 'Mars', 'neptune'])
st.select_slider('Pick a mark using this Select slider', ['Bad', 'Good', 'Excellent'])
st.slider('Pick a number using this numerical Slider', 0,50)

st.number_input('Enter a number', 0,10)
st.text_input('Email address')
st.date_input('Travelling date')
st.time_input('School time')
st.text_area('Description')
st.file_uploader('Upload a photo')
st.color_picker('Choose your favorite color')

if st.button("Click this for some balloons"):
    st.balloons()
st.progress(10)
with st.spinner('Wait for it...'):    
    time.sleep(3)
    
st.success("You did it !")
st.error("Error")
st.warning("Warning")
st.info("It's easy to build a streamlit app")
st.exception(RuntimeError("RuntimeError exception ;-) "))