import streamlit as st
import tempfile
import os
from utils.pose_estimation import extract_and_visualize_pose

st.set_page_config(page_title="投籃影片3D視覺化", layout="centered")

st.title("🏀 上傳你的投籃影片，3D動作視覺化")

video_file = st.file_uploader("請上傳投籃影片（mp4）", type=["mp4"])

if video_file:
    tfile = tempfile.NamedTemporaryFile(delete=False)
    tfile.write(video_file.read())
    video_path = tfile.name

    st.video(video_path)

    with st.spinner("分析中，請稍候..."):
        output_html = extract_and_visualize_pose(video_path)
        st.components.v1.html(output_html, height=600, scrolling=True)
