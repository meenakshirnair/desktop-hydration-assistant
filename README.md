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

## 🎨 Creating Your Custom Character with AI
If you want to create your own personalized pixel character using an AI image generator (like Google Gemini, Midjourney, or DALL-E), you can use the prompt formula below to get the perfect format.

## 🤖 The Generation Prompt
Prompt: A full-body 2D pixel art sprite sheet character of a [describe yourself/character, e.g., young woman with long dark brown hair wearing a black knitted sweater and black cargo pants OR add your image as reference]. The character should be standing, facing forward, holding a green water cup. Clean, solid white background, high-resolution pixel art, 16-bit retro video game aesthetic, asset isolated. No shadows, no gradients.

## ✂️ Prepping Your Files for the Script
Once your AI generates the image, follow these quick steps to make it work with the python script:

1. Remove the Background: Use a free background remover (like remove.bg) to turn the solid white background into a crisp, transparent canvas.

2. Crop Tight: Crop the image close to the boundaries of the character so there isn't excess empty space padding the files.

3. Save Your Formats:
-Save one single image holding the cup as static_drinking.png and place it in your assets/ folder.
-If you want to animate a walking sequence, slice your asset sheet into consecutive moving frames and drop them sequentially inside assets/frames/ (frame_0.png, frame_1.png, etc.).
