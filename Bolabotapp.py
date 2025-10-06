import streamlit as st

# App title
st.title("💬 BolaBot")

# Introduction
st.write("Hello! I'm your AI assistant for financial inclusion in Africa. Ask me anything about access to finance, savings, or microloans.")

# Input box
user_input = st.text_input("Type your message below:")

# When user clicks 'Send'
if st.button("Send"):
    if user_input.strip() == "":
        st.warning("Please type something before sending.")
    else:
        st.write("**You said:**", user_input)
        st.write("**BolaBot:** I'm still learning! I’ll get smarter with time 😄")
