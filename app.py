import streamlit as st
from streamlit_webrtc import webrtc_streamer, VideoTransformerBase
from fer import FER
import cv2

st.set_page_config(page_title="Real-time Emotion Detection", layout="centered")
st.title("Real-Time Emotion Detection (Webcam)")

st.markdown("""
Allow your browser to use the webcam when prompted.
""")

class EmotionDetector(VideoTransformerBase):
    def __init__(self):
        # create detector once
        self.detector = FER()

    def transform(self, frame):
        # frame -> numpy BGR image
        img = frame.to_ndarray(format="bgr24")
        try:
            # detect faces & emotions
            results = self.detector.detect_emotions(img)
            for face in results:
                x, y, w, h = face["box"]
                # sanitize coordinates
                x, y, w, h = max(0, x), max(0, y), max(0, w), max(0, h)
                # draw bbox
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
                # pick top emotion
                emotion, score = max(face["emotions"].items(), key=lambda kv: kv[1])
                label = f"{emotion} {int(score*100)}%"
                cv2.putText(img, label, (x, y - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
        except Exception as e:
            # don't crash the streamer
            print("Detection error:", e)
        return img

webrtc_streamer(
    key="emotion",
    video_processor_factory=EmotionDetector,  # updated here
    media_stream_constraints={"video": True, "audio": False},
)
