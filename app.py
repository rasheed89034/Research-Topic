# import streamlit as st
# import cv2
# from ultralytics import YOLO
# import math

# # ==========================================
# # 1. PAGE CONFIGURATION
# # ==========================================
# st.set_page_config(
#     page_title="CCTV Anomaly Pro | TriSense AI", 
#     page_icon="🛡️", 
#     layout="wide"
# )

# # ==========================================
# # 2. LOAD TRAINED MODEL
# # ==========================================
# @st.cache_resource
# def load_model():
#     # Make sure your latest model path is correct here
#     model_path = "best.pt"
#     return YOLO(model_path)

# model = load_model()

# # ==========================================
# # 3. PROFESSIONAL SIDEBAR DESIGN
# # ==========================================
# # Company Branding
# st.sidebar.markdown("<h1 style='text-align: center; color: #FF4B4B;'>🛡️ TriSense AI</h1>", unsafe_allow_html=True)
# st.sidebar.markdown("<p style='text-align: center; color: gray;'>Intelligent Vision Solutions</p>", unsafe_allow_html=True)
# st.sidebar.markdown("---")

# # Project Details Section (Expandable)
# with st.sidebar.expander("ℹ️ Project Details", expanded=False):
#     st.info("""
#     **CCTV Anomaly Pro** is a real-time AI surveillance engine. 
#     It continuously analyzes camera feeds to detect hazardous situations and anomalies instantly.
#     """)
#     st.markdown("""
#     **Detects:**
#     - 🔥 Fire & Smoke
#     - 🔫 Armed Violence (Gun)
#     - 🏃 Fall Detection
#     - ✅ Normal Activities
#     """)

# st.sidebar.markdown("---")

# # Control Panel
# st.sidebar.header("⚙️ Core Settings")
# run_camera = st.sidebar.toggle("🔴 Start Live Camera", value=False) # Toggle switch looks more professional than checkbox
# conf_threshold = st.sidebar.slider("🎯 Confidence Threshold", min_value=0.10, max_value=1.00, value=0.65, step=0.05)

# st.sidebar.markdown("---")

# # System Info
# st.sidebar.header("🖥️ System Specs")
# st.sidebar.code("Model   : YOLOv8s-cls (Pro)\nEngine  : PyTorch\nLatency : Real-time")

# st.sidebar.markdown("---")

# # Footer
# st.sidebar.markdown("<p style='text-align: center; font-size: 12px;'>Developed by <b>TriSense AI</b><br>© 2026 All Rights Reserved.</p>", unsafe_allow_html=True)


# # ==========================================
# # 4. MAIN DASHBOARD UI
# # ==========================================
# st.title("🚨 CCTV Anomaly Pro - Command Center")
# st.markdown("Real-time AI surveillance monitoring for critical environments.")
# st.markdown("---")

# col1, col2 = st.columns([2, 1])

# with col1:
#     st.subheader("📷 Live Camera Feed")
#     # Streamlit image placeholder
#     frame_window = st.image([], use_container_width=True)

# with col2:
#     st.subheader("📊 Live Telemetry")
#     status_text = st.empty()
#     alert_box = st.empty()
    
#     st.markdown("---")
#     st.markdown("### 🔔 Recent Logs")
#     # A placeholder for log styling
#     log_box = st.empty()
#     log_box.code("System Initialized...\nWaiting for camera feed...")

# # ==========================================
# # 5. LIVE CAMERA PROCESSING
# # ==========================================
# camera = cv2.VideoCapture(0)

# while run_camera:
#     ret, frame = camera.read()
#     if not ret:
#         st.error("⚠️ Camera access failed! Please check your webcam permissions.")
#         break
        
#     results = model(frame, verbose=False)
#     result = results[0]
    
#     probs = result.probs
#     top1_index = probs.top1
#     top1_conf = float(probs.top1conf)
#     class_name = result.names[top1_index]
    
#     if top1_conf >= conf_threshold:
        
#         status_text.markdown(f"**Current Detection:** `{class_name.upper()}`")
        
#         if class_name.lower() == "normal":
#             label = f"NORMAL ({math.floor(top1_conf * 100)}%)"
#             cv2.putText(frame, label, (20, 50), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 255, 0), 2)
#             alert_box.success("✅ **STATUS:** Environment Secure.")
#             log_box.code(f"[{class_name.upper()}] Confidence: {math.floor(top1_conf * 100)}%")
            
#         else:
#             label = f"{class_name.upper()} ({math.floor(top1_conf * 100)}%)"
#             cv2.putText(frame, label, (20, 50), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 255), 2)
#             alert_box.error(f"⚠️ **CRITICAL ALERT:** {class_name.upper()} detected!")
#             log_box.code(f"🚨 [{class_name.upper()}] Confidence: {math.floor(top1_conf * 100)}%\nAction: Security Notified.")
            
#     else:
#         status_text.markdown("**Current Detection:** `Scanning...`")
#         alert_box.info("🔍 Scanning environment...")
#         log_box.code("Scanning...")
    
#     frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#     frame_window.image(frame)

# else:
#     camera.release()
#     st.info("ℹ️ System is currently in standby mode. Toggle the camera switch in the Control Panel to start monitoring.")




# import streamlit as st
# import cv2
# from ultralytics import YOLO
# import numpy as np
# import tensorflow as tf
# import tensorflow_hub as hub
# import csv
# import os
# import av
# from streamlit_webrtc import webrtc_streamer, WebRtcMode, RTCConfiguration

# # YAMNet model ko cache karne ke liye
# os.environ["TFHUB_CACHE_DIR"] = "./model_cache"

# st.set_page_config(page_title="TriSense AI | Cloud Edition", page_icon="🛡️", layout="wide")



# import os
# # --- RAM & CPU OPTIMIZATION (SEGFAULT FIX) ---
# # AI ko majboor karein ke woh kam memory aur 1 thread use kare
# os.environ["OMP_NUM_THREADS"] = "1"
# os.environ["MKL_NUM_THREADS"] = "1"
# os.environ["TF_NUM_INTRAOP_THREADS"] = "1"
# os.environ["TF_NUM_INTEROP_THREADS"] = "1"

# # --- CRITICAL IMPORT ORDER ---
# import av  # Isay LAZMI cv2 aur torch se pehle import karna hai!
# import cv2 
# import streamlit as st
# from ultralytics import YOLO
# import numpy as np
# import tensorflow as tf
# import tensorflow_hub as hub
# import csv
# from streamlit_webrtc import webrtc_streamer, WebRtcMode, RTCConfiguration

# # TensorFlow ko strictly 1 thread tak mehdood karein
# tf.config.threading.set_intra_op_parallelism_threads(1)
# tf.config.threading.set_inter_op_parallelism_threads(1)

# # YAMNet model ko cache karne ke liye
# os.environ["TFHUB_CACHE_DIR"] = "./model_cache"

# st.set_page_config(page_title="TriSense AI | Cloud Edition", page_icon="🛡️", layout="wide")

# # ... (Baqi sara code waisa hi rahega jaisa pehle tha) ...

# # ==========================================
# # 1. LOAD MODELS
# # ==========================================
# @st.cache_resource
# def load_vision_model():
#     return YOLO("best.pt")

# @st.cache_resource
# def load_audio_model():
#     model = hub.load('https://tfhub.dev/google/yamnet/1')
#     class_map_path = model.class_map_path().numpy().decode('utf-8')
#     class_names = []
#     with tf.io.gfile.GFile(class_map_path) as csvfile:
#         reader = csv.DictReader(csvfile)
#         for row in reader:
#             class_names.append(row['display_name'])
#     return model, class_names

# vision_model = load_vision_model()
# audio_model, audio_classes = load_audio_model()

# RISKY_SOUNDS = ["Gunshot, gunfire", "Explosion", "Screaming", "Glass", "Siren", "Emergency vehicle", "Fire alarm"]

# # WebRTC STUN Server (Internet par camera connect karne ke liye)
# RTC_CONFIGURATION = RTCConfiguration(
#     {"iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]}
# )

# # ==========================================
# # 2. UI DESIGN
# # ==========================================
# st.markdown("🚨 TriSense AI - Cloud CCTV", unsafe_allow_html=True)
# st.markdown("WebRTC Enabled: Now accessing live camera and audio over the internet.", unsafe_allow_html=True)
# st.markdown("---")

# col1, col2 = st.columns([1, 3])
# with col1:
#     st.info("⚙️ **Settings**")
#     conf_threshold = st.slider("🎯 Vision Threshold", min_value=0.10, max_value=1.00, value=0.20, step=0.05)
#     st.markdown("Toggle 'START' on the video player to grant camera/mic permissions.", unsafe_allow_html=True)

# # Audio Text ko Video Thread tak pohnchane ke liye class
# class AudioState:
#     text = "Scanning..."
#     color = (255, 255, 255) # Default White

# audio_state = AudioState()

# # ==========================================
# # 3. WEBRTC PROCESSORS
# # ==========================================

# # A. Video Processing Loop
# def video_frame_callback(frame: av.VideoFrame) -> av.VideoFrame:
#     img = frame.to_ndarray(format="bgr24")
    
#     # Vision Prediction
#     results = vision_model(img, verbose=False)
#     top1_index = results[0].probs.top1
#     top1_conf = float(results[0].probs.top1conf)
#     vision_class = results[0].names[top1_index]
    
#     # Draw Vision Status on Camera Feed
#     if top1_conf >= conf_threshold:
#         v_label = f"VISION: {vision_class.upper()} ({int(top1_conf * 100)}%)"
#         v_color = (0, 255, 0) if vision_class.lower() == "normal" else (0, 0, 255)
#         cv2.putText(img, v_label, (20, 50), cv2.FONT_HERSHEY_DUPLEX, 0.8, v_color, 2)
#     else:
#         cv2.putText(img, "VISION: Scanning...", (20, 50), cv2.FONT_HERSHEY_DUPLEX, 0.8, (255, 255, 255), 2)
        
#     # Draw Audio Status on Camera Feed
#     cv2.putText(img, f"AUDIO: {audio_state.text}", (20, 90), cv2.FONT_HERSHEY_DUPLEX, 0.8, audio_state.color, 2)
    
#     return av.VideoFrame.from_ndarray(img, format="bgr24")

# # B. Audio Processing Loop
# def audio_frame_callback(frame: av.AudioFrame) -> av.AudioFrame:
#     audio_array = frame.to_ndarray().flatten()
    
#     # WebRTC generally uses 48000Hz, YAMNet needs 16000Hz. (Downsampling by taking every 3rd sample)
#     if frame.sample_rate == 48000:
#         audio_chunk = audio_array[::3].astype(np.float32)
#     else:
#         audio_chunk = audio_array.astype(np.float32)
        
#     # Normalization
#     max_amp = np.max(np.abs(audio_chunk))
#     if max_amp > 0.01:
#         audio_chunk = audio_chunk / max_amp
        
#     # Model Prediction
#     scores, _, _ = audio_model(audio_chunk)
#     top_class_index = tf.math.argmax(scores[0]).numpy()
#     top_class_name = audio_classes[top_class_index]
#     conf = float(scores[0][top_class_index].numpy())
    
#     if conf > 0.50 and top_class_name != "Silence":
#         is_alert = any(risk in top_class_name for risk in RISKY_SOUNDS)
#         audio_state.text = f"{top_class_name.upper()} ({int(conf * 100)}%)"
#         audio_state.color = (0, 0, 255) if is_alert else (255, 255, 255)
#     elif conf < 0.20:
#         audio_state.text = "Scanning..."
#         audio_state.color = (255, 255, 255)
        
#     return frame

# # ==========================================
# # 4. WEBRTC STREAMER LAUNCH
# # ==========================================
# with col2:
#     webrtc_streamer(
#         key="trisense_cctv",
#         mode=WebRtcMode.SENDRECV,
#         rtc_configuration=RTC_CONFIGURATION,
#         video_frame_callback=video_frame_callback,
#         audio_frame_callback=audio_frame_callback,
#         media_stream_constraints={"video": True, "audio": True},
#         async_processing=True
#     )


import os
import av
import cv2 
import streamlit as st
from ultralytics import YOLO
import numpy as np
from streamlit_webrtc import webrtc_streamer, WebRtcMode, RTCConfiguration

st.set_page_config(page_title="TriSense AI | Vision Only", page_icon="👁️", layout="wide")

# ==========================================
# LOAD VISION MODEL ONLY (Saves RAM)
# ==========================================
@st.cache_resource
def load_vision_model():
    return YOLO("best.pt")

vision_model = load_vision_model()

RTC_CONFIGURATION = RTCConfiguration(
    {"iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]}
)

st.markdown("<h1 style='text-align: center; color: #FF4B4B;'>🚨 TriSense AI - Cloud CCTV (Vision Only)</h1>", unsafe_allow_html=True)
st.markdown("---")

col1, col2 = st.columns([1, 3])
with col1:
    conf_threshold = st.slider("🎯 Vision Threshold", min_value=0.10, max_value=1.00, value=0.20, step=0.05)

# ==========================================
# WEBRTC PROCESSOR
# ==========================================
def video_frame_callback(frame: av.VideoFrame) -> av.VideoFrame:
    img = frame.to_ndarray(format="bgr24")
    
    results = vision_model(img, verbose=False)
    top1_index = results[0].probs.top1
    top1_conf = float(results[0].probs.top1conf)
    vision_class = results[0].names[top1_index]
    
    if top1_conf >= conf_threshold:
        v_label = f"VISION: {vision_class.upper()} ({int(top1_conf * 100)}%)"
        v_color = (0, 255, 0) if vision_class.lower() == "normal" else (0, 0, 255)
        cv2.putText(img, v_label, (20, 50), cv2.FONT_HERSHEY_DUPLEX, 0.8, v_color, 2)
    else:
        cv2.putText(img, "VISION: Scanning...", (20, 50), cv2.FONT_HERSHEY_DUPLEX, 0.8, (255, 255, 255), 2)
        
    return av.VideoFrame.from_ndarray(img, format="bgr24")

with col2:
    webrtc_streamer(
        key="trisense_cctv",
        mode=WebRtcMode.SENDRECV,
        rtc_configuration=RTC_CONFIGURATION,
        video_frame_callback=video_frame_callback,
        media_stream_constraints={"video": True, "audio": False}, # Audio False kiya hai
        async_processing=True
    )









