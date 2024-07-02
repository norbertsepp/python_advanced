import streamlit as st
import time

st.header("Lesson on streamlit layouts:\nSidebar, Columns, Expander")


def clean_text(text):
    cleaned = text.replace("`", "").replace("-\n", "").replace("\n", " ").strip()
    return cleaned
    
    
def generate_text():
    for t in "This was the best of times, this was the worst of times":
        time.sleep(0.03)
        yield t
        
st.write_stream(generate_text)       
st.sidebar.header("This is the header")
st.sidebar.image("https://www.python.org/static/community_logos/python-logo-master-v3-TM.png", width=300, caption="The Python Logo")
text = st.sidebar.text_area("Paste text here")
button1 = st.sidebar.button("Clean text")

# SIDEBAR
# if button1:
#     st.write(text)
#     clean = clean_text(text)
#     st.write(clean)

# COLUMNS
# if button1:
#     col1, col2, col3 = st.columns((0.3, 0.6, 0.1))
#     col1.header("Original text")
#     col1.write(text)
#     col2.header("Sanitized text")
#     clean = clean_text(text)
#     col2.write(clean)
#     col3.caption("Cool!")

# EXPANDER without with
# if button1:
#     col1, col2 = st.columns(2)
#     col1_expander = col1.expander("Click to see original")

#     col1_expander.header("Original Text")
#     col1_expander.write(text)
#     col2.header("Sanitized text")
#     clean = clean_text(text)
#     col2.write(clean)

# EXPANDER with with
if button1:
    col1, col2 = st.columns(2)
    col1_expander = col1.expander("Expand Original")
    with col1_expander:
        st.write(text)
    col2_expander = col2.expander("Expand Cleaned")
    clean = clean_text(text)
    col2_expander.write(clean)