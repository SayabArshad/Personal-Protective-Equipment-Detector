
# 🛡️ Personal Protective Equipment (PPE) Detector | Intelligent Safety Monitoring 🤖  
![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python) ![Tkinter](https://img.shields.io/badge/Framework-Tkinter-orange?logo=python) ![OpenCV](https://img.shields.io/badge/OpenCV-Computer%20Vision-red?logo=opencv) ![YOLOv8](https://img.shields.io/badge/Model-YOLOv8-green?logo=ultralytics) ![License](https://img.shields.io/badge/License-MIT-yellow) ![Status](https://img.shields.io/badge/Status-Active-brightgreen)  

<p align="center">
  <img src="https://cdn-icons-png.flaticon.com/512/2936/2936757.png" alt="PPE Detector Logo" width="140"/>
</p>

🚀 The **Personal Protective Equipment (PPE) Detector** is an AI-powered desktop application built using **YOLOv8**, **OpenCV**, and **Tkinter** that automatically detects safety equipment such as **helmets, masks, and vests** in real time.  
It ensures workplace safety by identifying compliance and violations, helping industries maintain safety standards efficiently.  

---

## ✨ Key Features  
🎥 **Live Detection** via webcam  
📁 **Upload Photo/Video** for offline PPE analysis  
🎛️ **Detection Modes:** All PPE, Helmets only 🪖, Masks only 😷, Vests only 🦺  
✅ **Compliance & Violation Alerts** (e.g., Hardhat vs. NO-Hardhat)  
🎨 **Color-coded Bounding Boxes** for easy visual differentiation  
🔔 **Instant Safety Notifications** for violations  
🧠 **YOLOv8 Smart Detection** for high-accuracy object recognition  

---

## 🧠 Tech Stack  
- **Language:** Python 🐍  
- **Framework:** Tkinter 🪟  
- **Libraries:** OpenCV 🎥, cvzone 🔧, YOLOv8 🤖  
- **Recommended IDE:** PyCharm / VS Code 💻  

---

## 📦 Installation  
```bash
git clone https://github.com/SayabArshad/Personal-Protective-Equipment-Detector.git
cd ppe-detector
pip install -r requirements.txt
````

> ⚙️ **Note:** Download your YOLO model (e.g., `PPE.pt`) and update its path in the script.

---

## ▶️ Usage

```bash
python ppe_detector.py
```

🎬 **Live Detection** → Starts webcam monitoring
📤 **Upload Mode** → Analyze images or videos offline
⏹️ Press **q** to stop detection

---

## 📁 Project Structure

```
ppe-detector/
│-- ppe_detector.py     # Main script
│-- requirements.txt    # Dependencies
│-- README.md           # Documentation
│-- PPE.pt              # YOLO model (user-provided)
│-- assets/             # Interface images
│    ├── 1.jpg
│    ├── 2.jpg
│    ├── 3.jpg
│    ├── 4.jpg
```

---

## 🖼️ Interface Previews

|       🧰 Settings Panel       |        🧠 Video Detection        |
| :--------------------------: | :--------------------------: |
| ![Interface 1](assets/1.JPG) | ![Interface 2](assets/2.jpg) |

|     ⚙️ Detection Results     |       🧰 Live Detection       |
| :--------------------------: | :--------------------------: |
| ![Interface 3](assets/3.jpg) | ![Interface 4](assets/4.jpg) |

---

## 💡 About the Project

The **PPE Detector** leverages cutting-edge **AI object detection** with **YOLOv8** and **OpenCV** to identify safety gear in real-time environments.
It is ideal for industrial, construction, and laboratory environments, ensuring compliance with workplace safety protocols.
Built with a lightweight **Tkinter interface**, it provides smooth operation and instant feedback for both live and offline modes.

---

## 🧑‍💻 Author

**Developed by:** [Sayab Arshad Soduzai](https://github.com/SayabArshad) 👨‍💻
📅 **Version:** 1.0.0
📜 **License:** MIT License

---

## ⭐ Contributions

Contributions are welcome! Fork the repository, open issues, or submit pull requests to improve the tool.
If you find this project useful, don’t forget to ⭐ **star the repository** to show your support.

---

## 📧 Contact

For queries, collaborations, or feedback, reach out at **[sayabarshad789@gmail.com](mailto:sayabarshad789@gmail.com)**

---

> 🦺 *Empowering safer workplaces through intelligent AI-based PPE monitoring.*
```
