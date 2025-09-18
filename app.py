import streamlit as st
import requests

st.title("AI Blog Writer with Optional Translation")

title = st.text_input("Title")
tone = st.selectbox("Tone", ["friendly", "informative", "professional"])
keywords = st.text_input("Keywords (comma separated)")
length = st.selectbox("Length", ["short", "medium", "long"])
humanize = st.checkbox("Human-like style", True)

# Optional translation
translate = st.checkbox("Translate blog into another language?")
target_language = None
if translate:
    target_language = st.text_input("Target Language", "French")

if st.button("Generate Blog"):
    payload = {
        "title": title,
        "tone": tone,
        "keywords": keywords,
        "length": length,
        "humanize": humanize,
        "target_language": target_language
    }
    response = requests.post("http://127.0.0.1:8000/generate", json=payload)
    if response.status_code == 200:
        st.success("✅ Blog Generated!")
        st.text_area("Draft", value=response.json()["draft"], height=400)
    else:
        st.error(response.text)
