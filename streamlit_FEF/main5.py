import spacy
import streamlit as st 

def extract_entities(ent_types, text):
    results = []
    doc = nlp(text)
    for ent in doc.ents:
        if ent.label_ in ent_types:
            results.append((ent.text, 
                           ent.label_))
    return results

@st.cache_resource
def load_model(model_name):
    nlp = spacy.load(model_name)
    return nlp

nlp = load_model("en_core_web_lg")

st.title("Forms in streamlit")

form1 = st.sidebar.form(key="Options") 
form1.header("Parameters")
ent_types = form1.multiselect("Select the entities you want to extract", ["PERSON", "ORG", "GPE"])
form1.form_submit_button("Click me to analyze")
text = st.text_area("Sample text", "James enjoys playing footbal for Barca Academy in Barcelona")

hits = extract_entities(ent_types, text)
st.write(hits)