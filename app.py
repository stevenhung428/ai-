import streamlit as st
import tempfile
import os
from utils.pose_estimation import extract_and_visualize_pose

st.set_page_config(page_title="投籃影片3D視覺化", layout="centered")

st.title("🏀 上傳你的投籃影片，3D動作視覺化")

video_file = st.file_uploader("請上傳投籃影片（mp4）", type=["mp4"])

# 先建立一個佔位元件
html_placeholder = st.empty()

if video_file:
    tfile = tempfile.NamedTemporaryFile(delete=False)
    tfile.write(video_file.read())
    video_path = tfile.name

    st.video(video_path)

    with st.spinner("分析中，請稍候..."):
        output_html = extract_and_visualize_pose(video_path)
        # 每次先清空佔位，再顯示 html，避免重複疊加導致錯誤
        html_placeholder.empty()
        html_placeholder.components.v1.html(output_html, height=600, scrolling=True)

