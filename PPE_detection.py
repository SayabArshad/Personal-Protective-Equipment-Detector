import tkinter as tk
from tkinter import filedialog, ttk
import cv2
import cvzone
import os
import math
from ultralytics import YOLO
import threading

# Load YOLO model
model_path = r"D:\python_ka_chilla\DIP project\PPE.pt"
if not os.path.exists(model_path):
    raise FileNotFoundError(f"Model file not found: {model_path}")
model = YOLO(model_path)

classNames = ['Hardhat', 'Mask', 'Person', 'Safety Vest', 'NO-Mask', 'NO-Hardhat',
              'Safety Cone', 'NO-Safety Vest', 'machinery', 'vehicle']

class PPEDetectorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("PPE Detector")
        self.root.geometry("950x600")
        self.root.configure(bg="#ffffff")
        self.video_thread = None
        self.stop_event = threading.Event()
        self.selected_mode = tk.StringVar(value="All PPE Items")

        # Main container
        self.main_frame = tk.Frame(root, bg="#ffffff")
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        # Header Section
        header_frame = tk.Frame(self.main_frame, bg="#003366")
        header_frame.pack(fill=tk.X, pady=(0, 20))

        self.title_label = tk.Label(
            header_frame,
            text="🛡️ PPE DETECTOR - INTELLIGENT SAFETY MONITORING",
            font=("Helvetica", 20, "bold"),
            fg="white",
            bg="#003366",
            pady=15
        )
        self.title_label.pack()

        # Detection Mode Selector
        mode_frame = tk.Frame(self.main_frame, bg="#99ccff")
        mode_frame.pack(pady=(20, 10))
        
        mode_label = tk.Label(
            mode_frame,
            text="Select Detection Mode:",
            font=("Helvetica", 12),
            bg="#99ccff"
        )
        mode_label.pack(side=tk.LEFT, padx=(0, 10))

        self.mode_selector = ttk.Combobox(
            mode_frame,
            textvariable=self.selected_mode,
            values=["All PPE Items", "Safety Helmets Only", "Protective Masks Only", "Safety Vests Only"],
            state="readonly",
            width=25,
            font=("Helvetica", 12)
        )
        self.mode_selector.pack(side=tk.LEFT)

        # Buttons Frame
        self.button_frame = tk.Frame(self.main_frame, bg="#99ccff")
        self.button_frame.pack(pady=20)

        self.live_button = tk.Button(
            self.button_frame,
            text="🎥 Live Detection",
            font=("Helvetica", 14, "bold"),
            bg="#007bff",
            fg="white",
            width=20,
            height=2,
            bd=0,
            command=self.start_live_detection
        )
        self.live_button.grid(row=0, column=0, padx=20, pady=10)

        self.upload_button = tk.Button(
            self.button_frame,
            text="📁 Upload Photo or Video",
            font=("Helvetica", 14, "bold"),
            bg="#28a745",
            fg="white",
            width=20,
            height=2,
            bd=0,
            command=self.upload_video
        )
        self.upload_button.grid(row=0, column=1, padx=20, pady=10)

    def detect_ppe_in_video(self, video_source):
        self.stop_event.clear()
        cap = cv2.VideoCapture(video_source)
        
        try:
            while not self.stop_event.is_set():
                success, img = cap.read()
                if not success:
                    break

                results = model(img, stream=True)

                for r in results:
                    for box in r.boxes:
                        x1, y1, x2, y2 = map(int, box.xyxy[0])
                        conf = math.ceil(box.conf[0] * 100) / 100
                        cls = int(box.cls[0])
                        currentClass = classNames[cls]

                        # Filter based on selected mode
                        selected_mode = self.selected_mode.get()
                        if selected_mode != "All PPE Items":
                            if "Helmets" in selected_mode and "Hardhat" not in currentClass:
                                continue
                            if "Masks" in selected_mode and "Mask" not in currentClass:
                                continue
                            if "Vests" in selected_mode and "Vest" not in currentClass:
                                continue

                        # Color logic
                        if currentClass in ['NO-Hardhat', 'NO-Mask', 'NO-Safety Vest']:
                            myColor = (0, 0, 255)
                        elif currentClass in ['Hardhat', 'Mask', 'Safety Vest']:
                            myColor = (0, 255, 0)
                        elif currentClass == 'Person':
                            myColor = (255, 255, 0)
                        else:
                            myColor = (255, 0, 0)

                        # Validate coordinates
                        h, w = img.shape[:2]
                        x1, y1 = max(0, x1), max(0, y1)
                        x2, y2 = min(w, x2), min(h, y2)

                        cvzone.putTextRect(img, f'{currentClass} {conf}',
                                          (x1, max(35, y1)),
                                          scale=1, thickness=1,
                                          colorB=myColor, colorT=(255, 255, 255),
                                          colorR=myColor, offset=5)
                        cv2.rectangle(img, (x1, y1), (x2, y2), myColor, 3)

                cv2.imshow("PPE Detection", img)
                if cv2.waitKey(1) & 0xFF == ord('q') or self.stop_event.is_set():
                    break

        finally:
            cap.release()
            cv2.destroyAllWindows()
            self.stop_event.set()

    def start_live_detection(self):
        self.stop_event.clear()
        self.video_thread = threading.Thread(target=self.detect_ppe_in_video, args=(0,))
        self.video_thread.start()

    def upload_video(self):
        filepath = filedialog.askopenfilename(filetypes=[("Video files", "*.mp4 *.avi *.mov")])
        if filepath:
            self.stop_event.clear()
            self.video_thread = threading.Thread(target=self.detect_ppe_in_video, args=(filepath,))
            self.video_thread.start()

    def on_closing(self):
        self.stop_event.set()
        if self.video_thread and self.video_thread.is_alive():
            self.video_thread.join()
        self.root.destroy()

if __name__ == '__main__':
    root = tk.Tk()
    app = PPEDetectorApp(root)
    root.protocol("WM_DELETE_WINDOW", app.on_closing)
    root.mainloop()