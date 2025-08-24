# 🕊️ Drone vs Birds Detection using YOLOv8 + Flask

This project implements a **real-time object detection system** that can distinguish between **drones and birds** in the sky using a **YOLOv8 deep learning model**.  
It also provides a **Flask web application** where users can upload images or use their live webcam to run detections directly in the browser.

---

## 📂 Repository Structure

- **app.py** – Flask web application (backend server).  
- **best.pt** – Trained YOLOv8 model weights for drone vs bird detection.  
- **templates/** – HTML files for the Flask web interface.  
- **static/** – CSS, JavaScript, and images for the website.  

---

## ▶️ Running the Project

1. Clone this repository:
   ```bash
   git clone https://github.com/kaal-bhairav69/drone_vs_birds_detection.git
   cd drone_vs_birds_detection

---

## Install dependencies:

pip install -r requirements.txt

---

## Run the Flask app:
python app.py

---

## Open your browser at:
http://127.0.0.1:5000/

---

## 🔬 Features:
✅ Real-time detection via webcam.

✅ Upload and analyze images for drones/birds.

✅ YOLOv8 trained model for accurate classification.

✅ Flask web app with simple UI.
