# birthday_web.py
import streamlit as st
import time

# --- CONFIGURE DETAILS ---
friend_name = "SAMIT"          # Change this to your friend's name
your_name = "Arman"            # <-- Your name here
message = "Happy Birthday!"    # Main wish

# --- STREAMLIT PAGE SETTINGS ---
st.set_page_config(page_title="Birthday Wish", page_icon="🎂", layout="centered")

# --- TITLE / HEADER ---
st.markdown(
    f"<h1 style='text-align: center; color: #FF69B4;'>🎉 {message} {friend_name}! 🎉</h1>",
    unsafe_allow_html=True
)

# --- ASCII ART STYLE (for big text look) ---
art = r"""
   ____ _   _ ____ _____    _    
  / ___| | | |  _ \_   _|  / \   
 | |  _| | | | |_) || |   / _ \  
 | |_| | |_| |  __/ | |  / ___ \ 
  \____|\___/|_|    |_| /_/   \_\
"""

st.code(art, language="text")

# --- ANIMATION EFFECT ---
with st.empty():
    for i in range(3):
        st.markdown(
            f"<h2 style='text-align:center;color:#00BFFF;'>✨ {message} {friend_name} ✨</h2>",
            unsafe_allow_html=True
        )
        time.sleep(0.5)
        st.markdown("")
        time.sleep(0.2)

# --- FINAL MESSAGE ---
st.success(f"🎂 {message} {friend_name} — With love, {your_name} 💖")

st.balloons()
