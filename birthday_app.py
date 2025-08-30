import streamlit as st
from datetime import datetime
from streamlit_autorefresh import st_autorefresh

# --- CONFIG ---
MEETING_DATE = datetime(2026, 5, 16, 10, 0, 0)   # date you meet again
REL_START = datetime(2021, 6, 12, 0, 0, 0)       # relationship start date

# --- PAGE SETUP ---
st.set_page_config(page_title="Happy Birthday My Love", page_icon="💕", layout="centered")
st.markdown("<h1 style='text-align: center; color: white;'>🎉 Happy Birthday My Love 🎉</h1>", unsafe_allow_html=True)

# Background color
st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(135deg, #ffb6c1, #ffc0cb, #ffdde1);
    }
    </style>
    """,
    unsafe_allow_html=True
)

# --- PLAYLIST ---
st.markdown("## 🎶 Choose a Song")
songs = {
    "Perfect – Ed Sheeran": "perfect.mp3",
    "Just the Way You Are – Bruno Mars": "just_the_way_you_are.mp3",
    "All of Me – John Legend": "all_of_me.mp3",
    "Happy Birthday 🎂": "happybirthday.mp3"
}
choice = st.radio("Pick a song to play:", list(songs.keys()))
st.audio(songs[choice], format="audio/mp3")

# --- AUTO REFRESH ---
st_autorefresh(interval=1000, limit=None, key="fancy_timer")  # refresh every 1 sec

# --- COUNTDOWN ---
st.markdown("## 💖 Countdown Until We Meet 💖")

now = datetime.now()

# Countdown until meeting
diff = MEETING_DATE - now
days = diff.days
seconds = diff.seconds
hours = seconds // 3600
minutes = (seconds % 3600) // 60
secs = seconds % 60

# Time together
diff2 = now - REL_START
days2 = diff2.days
seconds2 = diff2.seconds
hours2 = seconds2 // 3600
minutes2 = (seconds2 % 3600) // 60
secs2 = seconds2 % 60

# Show countdown
st.markdown(
    f"<div style='text-align:center; background:#B2E4ED; padding:10px; border-radius:10px;'>"
    f"⏳ {days} days, {hours} hours, {minutes} minutes, {secs} seconds</div>",
    unsafe_allow_html=True
)

# Show time together
st.markdown(
    f"<div style='text-align:center; background:#CEC0F0; padding:10px; border-radius:10px;'>"
    f"💑 {days2} days, {hours2} hours, {minutes2} minutes, {secs2} seconds together 💕</div>",
    unsafe_allow_html=True
)

# --- PHOTOS ---
st.markdown("## 📸 Our Memories")
photos = ["pic1.png", "pic2.png", "pic3.png"]  # Make sure these are in the same folder
st.image(photos, caption=["Memory 1", "Memory 2", "Memory 3"], use_container_width=True)

# --- MESSAGE ---
st.markdown("### 🥰 Every second with you is special. Can't wait to see you again! 💕")
