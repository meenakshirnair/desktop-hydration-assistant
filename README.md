# 🚰 Custom Desktop Hydration Assistant

A transparent, borderless macOS desktop companion built with Python and PySide6 that walks onto your screen to remind you to drink water!

## ✨ Features
- Fully animated frame-by-frame asset pipeline.
- Bypasses macOS background focus blocks using native AppleScript integration.
- Custom "Snooze (10m)" and "Got it! (1h)" repeating loop logic.
- Stays on top of all active application workspaces.

## 🛠️ Setup & Installation
1. Clone or fork this repository.
2. Install the requirements:
   ```bash
   pip install PySide6
3. Put your own sequential animation images inside the assets/frames/ directory (frame_0.png, frame_1.png, etc.).
4. Run the script:
   ```bash
   python hydration_reminder.py
