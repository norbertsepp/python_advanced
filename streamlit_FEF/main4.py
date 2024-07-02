import spacy
import streamlit as st 

nlp = spacy.load("en_core_web_lg")
# poblematic: large file loads up every time sg is changed on the webapp.

def extract_entities(ent_types, text):
    results = []
    doc = nlp(text)
    for ent in doc.ents:
        if ent.label_ in ent_types:
            results.append((ent.text, 
                           ent.label_))
    return results

st.title("Forms in streamlit")

# VERSION 1 - WAIT FOR CLICK - SLOOOOW
# st.sidebar.header("Parameters")
# ent_types = st.sidebar.multiselect("Select the entities you want to extract", ["PERSON", "ORG", "GPE"])
# text = st.text_area("Sample text", "James enjoys playing footbal for Barca Academy in Barcelona")
# if st.sidebar.button("Click me to analyze"):
#     hits = extract_entities(ent_types, text)
#     st.write(hits)

# VERSION 2 - USING FORMS

form1 = st.sidebar.form(key="Options") 
form1.header("Parameters")
ent_types = form1.multiselect("Select the entities you want to extract", ["PERSON", "ORG", "GPE"])
form1.form_submit_button("Click me to analyze")
text = st.text_area("Sample text", "James enjoys playing footbal for Barca Academy in Barcelona")

hits = extract_entities(ent_types, text)
st.write(hits)