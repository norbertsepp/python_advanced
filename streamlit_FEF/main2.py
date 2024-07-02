# SECTION 1
import streamlit as st
st.title("This is a Streamlit TUTORIAL")
st.write("hi, this is streamlit running!:", st.__version__)
st.header("Some nice st stuff")
chk1 = st.checkbox("Do you like streamlit?")
button1 = st.button("Submit")
if button1:
    if chk1:
        st.write("Happy to hear that!")
    else:
        st.write("Grrrr")

st.header("Radio buttons")
radio1 = st.radio("What is your favourite programming language?", ("Python", "Java", "Rust", "Go", "C++", "Haskell"))
if radio1 == "Python":
    st.write("Good user")
    
    
# SECTION 2

def analyze_text_sentiment(txt):
    return "Analysis DONE."

st.header("This is the section for multiinput, slider, num_input, text_area, processing function")
bands = st.multiselect("Select your favourite bands", ["Beatles", "ABBA", "Led Zeppelin", "Elefant", "Quimby", "U2"])
epochs_num = st.slider("How many epochs should we run?", 1, 100, 15)
if st.button("Submit epochs"):
    st.write(f"We will run {epochs_num} epochs for your bands:\n", bands)
    
my_num = st.number_input("How many times have you read SWIV?", 2)
my_text = st.text_area("Text to analyze", 
                       '''A long time ago, in a galax far, far away... 
                       The hope of freedom was kept alive by Rebel Forces
                       fighting against the evil Galactic Empire''')
st.write("Sentiment: ", analyze_text_sentiment(my_text), '---', my_num)