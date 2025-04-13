import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Chatbot", layout="centered")
st.markdown("### 👋 Willkommen bei der Schreinerei GmbH")

frage = st.chat_input("Stellen Sie Ihre Frage:")

if frage:
    st.chat_message("user").markdown(frage)
    st.chat_message("assistant").markdown("🔧 Dies ist eine Beispielantwort.")
