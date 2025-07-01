# emotion_detection
# 😊 Emotion Detection Using Webcam

This is a simple Python project that uses your computer's webcam to detect human emotions in real-time.

It shows your face live on screen and tells if you're happy, sad, angry, or surprised — right while you're looking at the camera!

---

## 💻 What You Need

- A computer or laptop with a webcam
- Python installed (version 3.x)
- Required Python packages:
  - `opencv-python`
  - `fer`

---

## 🔧 How to Use

### Step 1: Install the required packages

Open your terminal or command prompt and run:

pip install opencv-python fer


### Step 2: Run the app

In the same terminal, run:

python app.py


Your webcam will open in a new window, and it will detect your face and show your emotion like:
happy (0.95)
angry (0.88)


---

## ❌ How to Stop

Press the **`q`** key on your keyboard to close the webcam window and exit the program.

---

## 🧠 What’s Happening Inside

- The program uses the **FER (Facial Emotion Recognition)** library to detect emotions.
- **OpenCV** is used to:
  - Access your webcam
  - Draw rectangles around your face
  - Display your emotion on the screen

---

## 📂 Files in this Project

- `app.py` → This is the main file that starts the webcam and performs emotion detection.

---

## 🧑‍💻 Author

Created with ❤️ by [priyan-18](https://github.com/priyan-18)

Feel free to use or improve this project!
