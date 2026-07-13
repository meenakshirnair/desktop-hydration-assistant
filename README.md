# 🚰 Custom Desktop Hydration Assistant

A transparent, borderless macOS desktop companion built with Python and PySide6 that walks onto your screen to remind you to drink water!

## ✨ Features
- Fully animated frame-by-frame asset pipeline.
- Bypasses macOS background focus blocks using native AppleScript integration.
- Custom "Snooze (10m)" and "Got it! (1h)" repeating loop logic.
- Stays on top of all active application workspaces.

## 🛠️ Step-by-Step Setup & Installation

Follow these exact steps to get your assistant running on your Mac desktop, even if you have never opened a terminal before!

### Step 1: Open Your Terminal
1. Press `Cmd + Space` on your keyboard to open Spotlight Search.
2. Type **Terminal** and press `Enter`. A blank text window will open.

### Step 2: Navigate to Your Folder
Type the following command into your terminal and press `Enter` (replace the path if you saved the downloaded folder somewhere other than your Downloads folder):
   ```bash
   cd ~/Downloads/desktop-hydration-assistant

### Step 3: Install Python Packages
Macs do not come with the required visual graphics tools pre-installed. Paste this command into your terminal and press Enter to install them:
   ```bash
   pip install PySide6
(Note: If your Mac says command not found: pip, run python3 -m pip install PySide6 instead!)

### Step 4: Test Run the Script
To make sure your images and character load properly, run this command to test it:

```bash
python3 hydration_reminder.py
Your character should instantly walk onto the bottom left side of your screen! Click Got it! to close it.

## 🚀 How to Make It Run Automatically in the Background
To make the character work silently in the background without needing the Terminal window open, we will turn it into a native Mac App.
Open Automator on your Mac (Press Cmd + Space, type "Automator", and press Enter).
Choose Application as your document type.
In the search bar on the left, type "Run Shell Script" and double-click it to add it to your workflow window.
Change the Shell dropdown menu from /bin/sh to /bin/zsh.

Paste the following text into the big box:
```bash
cd ~/Downloads/desktop-hydration-assistant
python3 hydration_reminder.py

Go to the top menu bar, click File > Save, name it "Hydration Reminder", and save it directly into your Mac's Applications folder.
To make it open automatically whenever you turn on your Mac, go to System Settings > General > Login Items, click the + (Plus) icon, and add your new app!

## 🎨 Creating Your Custom Character with AI
If you want to create your own personalized pixel character using an AI image generator (like Google Gemini, Midjourney, or DALL-E), you can use the prompt formula below to get the perfect format.

## 🤖 The Generation Prompt
Prompt: A full-body 2D pixel art sprite sheet character of a [describe yourself/character, e.g., young woman with long dark brown hair wearing a black knitted sweater and black cargo pants OR add your image as reference]. The character should be standing, facing forward, holding a green water cup. Clean, solid white background, high-resolution pixel art, 16-bit retro video game aesthetic, asset isolated. No shadows, no gradients.

## ✂️ Prepping Your Files for the Script
Once your AI generates the image, follow these quick steps to make it work with the python script:

#### 1. Remove the Background: 
Use a free background remover (like remove.bg) to turn the solid white background into a crisp, transparent canvas.

#### 2. Crop Tight: 
Crop the image close to the boundaries of the character so there isn't excess empty space padding the files.

#### 3. Save Your Formats:
- Save one single image holding the cup as static_drinking.png and place it in your assets/ folder.
- If you want to animate a walking sequence, slice your asset sheet into consecutive moving frames and drop them sequentially inside assets/frames/ (frame_0.png, frame_1.png, etc.).
