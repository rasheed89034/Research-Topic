# import streamlit as st
# import cv2
# from ultralytics import YOLO
# import math


# st.set_page_config(
#     page_title="CCTV Anomaly Pro", 
#     page_icon="🚨", 
#     layout="wide"
# )


# # 2. LOAD TRAINED MODEL

# @st.cache_resource
# def load_model():
#     # path
#     model_path = "runs/classify/AeroGuard/Vision_Model/weights/best.pt"
#     return YOLO(model_path)

# model = load_model()


# st.title("🚨 CCTV Anomaly Pro - Live Monitoring")
# st.markdown("Real-time AI surveillance for Fire, Smoke, Fall, and Violence detection.")
# st.markdown("---")

# # Sidebar for Controls
# st.sidebar.header("⚙️ Control Panel")
# run_camera = st.sidebar.checkbox("🟢 Start Live Camera")
# conf_threshold = st.sidebar.slider("Confidence Threshold", min_value=0.1, max_value=1.0, value=0.6, step=0.05)

# st.sidebar.markdown("---")
# st.sidebar.info("Developed by TriSense AI")


# col1, col2 = st.columns([2, 1])

# with col1:
#     st.subheader("📷 Live Camera Feed")
#     frame_window = st.image([])

# with col2:
#     st.subheader("📊 System Status")
#     status_text = st.empty()
#     alert_box = st.empty()


# # 4. LIVE CAMERA PROCESSING

# camera = cv2.VideoCapture(0)


# while run_camera:
#     ret, frame = camera.read()
#     if not ret:
#         st.error("⚠️ Camera access failed! Please check your webcam permissions.")
#         break
        
#     # YOLO Model Prediction 
#     results = model(frame, verbose=False)
#     result = results[0]
    
#     # (Top 1) mactch classes
#     probs = result.probs
#     top1_index = probs.top1
#     top1_conf = float(probs.top1conf)
#     class_name = result.names[top1_index]
    

#     if top1_conf >= conf_threshold:
        
   
#         label = f"{class_name.upper()} ({math.floor(top1_conf * 100)}%)"
#         cv2.putText(frame, label, (20, 50), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 255), 2)
        
        
#         status_text.markdown(f"**Current Detection:** `{class_name.upper()}`")
        
        
#         alert_box.error(f"⚠️ **ALERT:** {class_name.upper()} activity detected!")
#     else:
#         status_text.markdown("**Current Detection:** `Scanning...`")
#         alert_box.success("✅ System Secure. No anomaly detected.")
    
#     # OpenCV (BGR) color Streamlit (RGB) color  converting
#     frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    

#     frame_window.image(frame)


# else:
#     camera.release()
#     st.info("ℹ️ Camera is currently OFF. Check the box in the sidebar to start live monitoring.")


# import streamlit as st
# import cv2
# from ultralytics import YOLO
# import math

# # ==========================================
# # 1. PAGE CONFIGURATION
# # ==========================================
# st.set_page_config(
#     page_title="CCTV Anomaly Pro", 
#     page_icon="🚨", 
#     layout="wide"
# )

# # ==========================================
# # 2. LOAD TRAINED MODEL
# # ==========================================
# @st.cache_resource
# def load_model():
#     # ⚠️ UPDATE: Yahan humne naye 'Vision_Model_Pro' ka path de diya hai
#     model_path = "runs/classify/AeroGuard/Vision_Model_Pro/weights/best.pt"
#     return YOLO(model_path)

# model = load_model()

# # ==========================================
# # 3. DASHBOARD UI DESIGN
# # ==========================================
# st.title("🚨 CCTV Anomaly Pro - Live Monitoring")
# st.markdown("Real-time AI surveillance for Fire, Smoke, Fall, Violence, and Normal activity.")
# st.markdown("---")

# st.sidebar.header("⚙️ Control Panel")
# run_camera = st.sidebar.checkbox("🟢 Start Live Camera")
# conf_threshold = st.sidebar.slider("Confidence Threshold", min_value=0.1, max_value=1.0, value=0.6, step=0.05)
# st.sidebar.markdown("---")
# st.sidebar.info("Developed by Rasheed Ahmad")

# col1, col2 = st.columns([2, 1])

# with col1:
#     st.subheader("📷 Live Camera Feed")
#     frame_window = st.image([])

# with col2:
#     st.subheader("📊 System Status")
#     status_text = st.empty()
#     alert_box = st.empty()

# # ==========================================
# # 4. LIVE CAMERA PROCESSING
# # ==========================================
# camera = cv2.VideoCapture(0)

# while run_camera:
#     ret, frame = camera.read()
#     if not ret:
#         st.error("⚠️ Camera access failed! Please check your webcam permissions.")
#         break
        
#     # YOLO prediction
#     results = model(frame, verbose=False)
#     result = results[0]
    
#     probs = result.probs
#     top1_index = probs.top1
#     top1_conf = float(probs.top1conf)
#     class_name = result.names[top1_index]
    
#     # Confidence check
#     if top1_conf >= conf_threshold:
        
#         # UI Status Update
#         status_text.markdown(f"**Current Detection:** `{class_name.upper()}`")
        
#         # ⚠️ UPDATE: Agar model 'normal' detect kare toh red alert mat do
#         if class_name.lower() == "normal":
#             label = f"NORMAL ({math.floor(top1_conf * 100)}%)"
#             cv2.putText(frame, label, (20, 50), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 255, 0), 2) # Green text
#             alert_box.success("✅ System Secure. No anomaly detected.")
            
#         else:
#             # Agar koi anomaly (Gun, Fire, etc.) hai toh Red Alert do
#             label = f"{class_name.upper()} ({math.floor(top1_conf * 100)}%)"
#             cv2.putText(frame, label, (20, 50), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 255), 2) # Red text
#             alert_box.error(f"⚠️ **ALERT:** {class_name.upper()} activity detected!")
            
#     else:
#         status_text.markdown("**Current Detection:** `Scanning...`")
#         alert_box.info("🔍 Scanning environment...")
    
#     # Convert BGR to RGB for Streamlit
#     frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#     frame_window.image(frame)

# else:
#     camera.release()
#     st.info("ℹ️ Camera is currently OFF. Check the box in the sidebar to start live monitoring.")

import streamlit as st
import cv2
from ultralytics import YOLO
import math

# ==========================================
# 1. PAGE CONFIGURATION
# ==========================================
st.set_page_config(
    page_title="CCTV Anomaly Pro | TriSense AI", 
    page_icon="🛡️", 
    layout="wide"
)

# ==========================================
# 2. LOAD TRAINED MODEL
# ==========================================
@st.cache_resource
def load_model():
    # Make sure your latest model path is correct here
    model_path = "runs/classify/AeroGuard/Vision_Model_Pro/weights/best.pt"
    return YOLO(model_path)

model = load_model()

# ==========================================
# 3. PROFESSIONAL SIDEBAR DESIGN
# ==========================================
# Company Branding
st.sidebar.markdown("<h1 style='text-align: center; color: #FF4B4B;'>🛡️ TriSense AI</h1>", unsafe_allow_html=True)
st.sidebar.markdown("<p style='text-align: center; color: gray;'>Intelligent Vision Solutions</p>", unsafe_allow_html=True)
st.sidebar.markdown("---")

# Project Details Section (Expandable)
with st.sidebar.expander("ℹ️ Project Details", expanded=False):
    st.info("""
    **CCTV Anomaly Pro** is a real-time AI surveillance engine. 
    It continuously analyzes camera feeds to detect hazardous situations and anomalies instantly.
    """)
    st.markdown("""
    **Detects:**
    - 🔥 Fire & Smoke
    - 🔫 Armed Violence (Gun)
    - 🏃 Fall Detection
    - ✅ Normal Activities
    """)

st.sidebar.markdown("---")

# Control Panel
st.sidebar.header("⚙️ Core Settings")
run_camera = st.sidebar.toggle("🔴 Start Live Camera", value=False) # Toggle switch looks more professional than checkbox
conf_threshold = st.sidebar.slider("🎯 Confidence Threshold", min_value=0.10, max_value=1.00, value=0.65, step=0.05)

st.sidebar.markdown("---")

# System Info
st.sidebar.header("🖥️ System Specs")
st.sidebar.code("Model   : YOLOv8s-cls (Pro)\nEngine  : PyTorch\nLatency : Real-time")

st.sidebar.markdown("---")

# Footer
st.sidebar.markdown("<p style='text-align: center; font-size: 12px;'>Developed by <b>TriSense AI</b><br>© 2026 All Rights Reserved.</p>", unsafe_allow_html=True)


# ==========================================
# 4. MAIN DASHBOARD UI
# ==========================================
st.title("🚨 CCTV Anomaly Pro - Command Center")
st.markdown("Real-time AI surveillance monitoring for critical environments.")
st.markdown("---")

col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("📷 Live Camera Feed")
    # Streamlit image placeholder
    frame_window = st.image([], use_container_width=True)

with col2:
    st.subheader("📊 Live Telemetry")
    status_text = st.empty()
    alert_box = st.empty()
    
    st.markdown("---")
    st.markdown("### 🔔 Recent Logs")
    # A placeholder for log styling
    log_box = st.empty()
    log_box.code("System Initialized...\nWaiting for camera feed...")

# ==========================================
# 5. LIVE CAMERA PROCESSING
# ==========================================
camera = cv2.VideoCapture(0)

while run_camera:
    ret, frame = camera.read()
    if not ret:
        st.error("⚠️ Camera access failed! Please check your webcam permissions.")
        break
        
    results = model(frame, verbose=False)
    result = results[0]
    
    probs = result.probs
    top1_index = probs.top1
    top1_conf = float(probs.top1conf)
    class_name = result.names[top1_index]
    
    if top1_conf >= conf_threshold:
        
        status_text.markdown(f"**Current Detection:** `{class_name.upper()}`")
        
        if class_name.lower() == "normal":
            label = f"NORMAL ({math.floor(top1_conf * 100)}%)"
            cv2.putText(frame, label, (20, 50), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 255, 0), 2)
            alert_box.success("✅ **STATUS:** Environment Secure.")
            log_box.code(f"[{class_name.upper()}] Confidence: {math.floor(top1_conf * 100)}%")
            
        else:
            label = f"{class_name.upper()} ({math.floor(top1_conf * 100)}%)"
            cv2.putText(frame, label, (20, 50), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 255), 2)
            alert_box.error(f"⚠️ **CRITICAL ALERT:** {class_name.upper()} detected!")
            log_box.code(f"🚨 [{class_name.upper()}] Confidence: {math.floor(top1_conf * 100)}%\nAction: Security Notified.")
            
    else:
        status_text.markdown("**Current Detection:** `Scanning...`")
        alert_box.info("🔍 Scanning environment...")
        log_box.code("Scanning...")
    
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    frame_window.image(frame)

else:
    camera.release()
    st.info("ℹ️ System is currently in standby mode. Toggle the camera switch in the Control Panel to start monitoring.")