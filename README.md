🛡️ Personal Protective Equipment Detector – Intelligent Safety Monitoring

An AI-powered desktop app built with YOLOv8, OpenCV, and Tkinter to detect Personal Protective Equipment (PPE) such as helmets, masks, and safety vests in real time.

🚀 Features

🎥 Live Detection via webcam

📁 Upload Photo/Video for offline analysis

🎛️ Detection Modes: All PPE, Helmets only, Masks only, Vests only

✅ Compliance vs. Violation Alerts (e.g., Hardhat vs. NO-Hardhat)

🎨 Color-coded Bounding Boxes for quick identification

🛠️ Tech Stack

Python 3.8+

Tkinter (GUI)

OpenCV & cvzone (vision utilities)

Ultralytics YOLOv8 (object detection)

📦 Installation
git clone https://github.com/SayabArshad/Personal Protective Equipment Detector.git
cd ppe-detector
pip install -r requirements.txt


Download your YOLO model (e.g., PPE.pt) and update its path in the script.

▶️ Usage
python ppe_detector.py


Live Detection → starts webcam monitoring

Upload → analyze stored media

Press q to stop detection

📂 Structure
ppe-detector/
│-- ppe_detector.py     # Main script
│-- requirements.txt    # Dependencies
│-- README.md           # Documentation
│-- PPE.pt              # YOLO model (user-provided)

🧑‍💻 Author

Developed by [Sayab Arshad Soduzai]
🔗 GitHub: [Sayab Arshad](https://github.com/SayabArshad)
