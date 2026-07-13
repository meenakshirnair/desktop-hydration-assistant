import sys
import os
import re
from PySide6.QtCore import Qt, QTimer
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton
from PySide6.QtGui import QPixmap, QGuiApplication

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_IMAGE_PATH = os.path.join(SCRIPT_DIR, "assets", "static_drinking.png")
FRAMES_DIR = os.path.join(SCRIPT_DIR, "assets", "frames")

class HydrationReminder(QWidget):
    def __init__(self, interval_minutes=30):
        super().__init__()
        self.interval_ms = interval_minutes * 60 * 1000
        self.snooze_ms = 10 * 60 * 1000  
        
        # Configure fully transparent canvas parameters
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint | Qt.WindowType.WindowStaysOnTopHint | Qt.WindowType.Tool)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground, True)
        
        # FIX: Expanded width from 500 to 700 so the right side never cuts off!
        self.setFixedSize(700, 750)
        self.move_to_left_side()

        self.layout = QVBoxLayout()
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(15)
        self.layout.setAlignment(Qt.AlignmentFlag.AlignBottom | Qt.AlignmentFlag.AlignHCenter)
        self.setLayout(self.layout)
        
        # Character Viewport
        self.character_label = QLabel(self)
        self.character_label.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground, True)
        self.character_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.layout.addWidget(self.character_label)
        
        # Notification UI Box
        self.ui_container = QWidget()
        self.ui_container.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground, True)
        self.ui_layout = QVBoxLayout(self.ui_container)
        self.ui_layout.setContentsMargins(0, 0, 0, 0)
        self.ui_layout.setSpacing(10)
        self.ui_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        # Speech Bubble
        self.speech_bubble = QLabel("Time to hydrate! 🚰")
        self.speech_bubble.setStyleSheet("""
            QLabel {
                background-color: rgba(30, 30, 30, 0.9); 
                color: #FFFFFF; 
                padding: 10px 20px; 
                border-radius: 12px; 
                font-family: 'Courier New';
                font-weight: bold;
                font-size: 14px;
                border: 1px solid #555555;
            }
        """)
        self.speech_bubble.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.ui_layout.addWidget(self.speech_bubble)
        
        # Action Buttons Layout
        self.btn_layout = QHBoxLayout()
        self.btn_got_it = QPushButton("Got it!")
        self.btn_snooze = QPushButton("Snooze")
        
        button_style = """
            QPushButton {
                background-color: rgba(45, 45, 45, 0.95); 
                color: #FFFFFF; 
                border: 1px solid #555555; 
                padding: 8px 16px; 
                border-radius: 6px;
                font-family: 'Courier New';
                font-weight: bold;
                font-size: 12px;
            }
            QPushButton:hover {
                background-color: #555555;
            }
        """
        self.btn_got_it.setStyleSheet(button_style)
        self.btn_snooze.setStyleSheet(button_style)
        
        self.btn_layout.addWidget(self.btn_got_it)
        self.btn_layout.addWidget(self.btn_snooze)
        self.ui_layout.addLayout(self.btn_layout)
        
        self.layout.addWidget(self.ui_container)
        self.ui_container.hide() 
        
        self.btn_got_it.clicked.connect(self.reset_main_timer)
        self.btn_snooze.clicked.connect(self.trigger_snooze)
        
        # Internal Frame Animation Engine Setup
        self.animation_frames = []
        self.current_frame_index = 0
        self.load_animation_frames()
        
        self.frame_timer = QTimer()
        self.frame_timer.timeout.connect(self.next_frame)
        
        self.reminder_timer = QTimer()
        self.reminder_timer.timeout.connect(self.start_reminder_sequence)
        
        # --- TESTING MODE ---
        self.reminder_timer.start(self.interval_ms)

        # --- PRODUCTION MODE ---
        # 1. Force the reminder animation sequence to run instantly on startup
        self.start_reminder_sequence()

    def extract_number(self, filename):
        numbers = re.findall(r'\d+', filename)
        return int(numbers[0]) if numbers else 0

    def load_animation_frames(self):
        if not os.path.exists(FRAMES_DIR):
            return
        valid_files = [f for f in os.listdir(FRAMES_DIR) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
        valid_files.sort(key=self.extract_number)
        
        for file in valid_files:
            self.animation_frames.append(QPixmap(os.path.join(FRAMES_DIR, file)))

    def move_to_left_side(self):
        screen = QGuiApplication.primaryScreen().geometry()
        x = 0 
        y = screen.height() - self.height() - 80
        self.move(x, y)

    def force_macos_focus(self):
        try:
            script = 'tell application "System Events" to set frontmost of every process whose name is "Python" to true'
            os.system(f"osascript -e '{script}' > /dev/null 2>&1")
        except Exception:
            pass

    def start_reminder_sequence(self):
        self.reminder_timer.stop()
        self.ui_container.hide()
        
        if not self.animation_frames:
            self.show_static_phase()
            return
            
        self.show()
        self.raise_()
        self.activateWindow()
        self.force_macos_focus()
        
        self.current_frame_index = 0
        self.frame_timer.start(41) # Runs smoothly at ~24 FPS

    def next_frame(self):
        if self.current_frame_index < len(self.animation_frames):
            self.character_label.setPixmap(self.animation_frames[self.current_frame_index])
            self.current_frame_index += 1
        else:
            # FIX: Instead of looping back to frame 0, stop right here at the end frame!
            self.show_static_phase()

    def show_static_phase(self):
        self.frame_timer.stop()
        
        # Cleanly transition to the static pose
        pixmap = QPixmap(STATIC_IMAGE_PATH)
        self.character_label.setPixmap(pixmap)
        
        # 1-second clean pause gap
        QTimer.singleShot(1000, self.show_reminder_ui)

    def show_reminder_ui(self):
        self.ui_container.show()
        self.raise_()
        self.activateWindow()
        self.force_macos_focus()

    def reset_main_timer(self):
        self.hide()
        self.reminder_timer.start(self.interval_ms) 

    def trigger_snooze(self):
        self.hide()
        self.reminder_timer.start(self.snooze_ms) 

if __name__ == "__main__":
    app = QApplication(sys.argv)
    reminder = HydrationReminder(interval_minutes=60) 
    sys.exit(app.exec())
