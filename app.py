import streamlit as st

st.title("測試頁面")

placeholder = st.empty()

uploaded_file = st.file_uploader("上傳影片", type=["mp4"])

if uploaded_file:
    placeholder.video(uploaded_file)

