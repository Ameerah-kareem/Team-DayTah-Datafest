import streamlit as st

# App title
st.title("💬 BolaBot")

# Introduction
st.write(
    "Hello! I'm **BolaBot**, your friendly financial assistant. "
    "Ask me about Ajo, savings, or microloans. You can also switch my language below 👇"
)

# LANGUAGE TOGGLE
st.subheader("🌍 Choose BolaBot's Language")
language = st.radio(
    "Select Language:",
    ("English", "Pidgin", "Yoruba"),
    horizontal=True
)


# Input box
user_input = st.text_input("Type your message below:")

# When user clicks 'Send'
if st.button("Send"):
    if user_input.strip() == "":
        st.warning("Please type something before sending.")
    else:
        if language == "English":
            bot_reply = "Thanks for your message! I’ll get smarter with time 😄"
        elif language == "Pidgin":
            bot_reply = "I hear you well-well! I go sabi more soon 😄"
        elif language == "Yoruba":
            bot_reply = "Mo gbọ́ ọ, ẹ ṣéun! Emi yóò di ọlọ́gbọ́n laipẹ 😄"

        st.write(f"**You ({language}):** {user_input}")
        st.write(f"**BolaBot:** {bot_reply}")



