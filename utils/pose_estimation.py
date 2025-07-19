import cv2
import mediapipe as mp
import tempfile

def extract_and_visualize_pose(video_path):
    mp_pose = mp.solutions.pose
    pose = mp_pose.Pose(static_image_mode=False)
    mp_drawing = mp.solutions.drawing_utils

    cap = cv2.VideoCapture(video_path)
    html_frames = []

    while cap.isOpened():
        success, frame = cap.read()
        if not success:
            break

        results = pose.process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
        annotated_image = frame.copy()
        if results.pose_landmarks:
            mp_drawing.draw_landmarks(
                annotated_image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS
            )

        _, buffer = cv2.imencode('.jpg', annotated_image)
        b64_img = buffer.tobytes().hex()
        html_frames.append(f'<img src="data:image/jpeg;base64,{b64_img}" style="width:100%">')

    cap.release()
    return "<br>".join(html_frames)
