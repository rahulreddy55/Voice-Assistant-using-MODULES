# 🎙️ Voice Assistant in Python

This is a simple voice assistant built using Python. It can recognize your voice commands, respond with speech, and perform actions like opening websites or sending OTPs via email.

## 🚀 Features

- 🎤 Speech recognition using Google's API
- 🗣️ Text-to-speech responses using `pyttsx3`
- 🌐 Opens websites like Google, LinkedIn, and GitHub
- 🔐 Sends OTP to a user-entered email address
- 🤖 Interactive and continuously listens for commands

## 🛠️ Requirements

Install the required Python packages using pip:

```bash
pip install pyttsx3 SpeechRecognition pyaudio
Note: You may need to install PyAudio separately based on your OS. For Windows:

bash
Copy
Edit
pip install pipwin
pipwin install pyaudio
📁 Project Structure
bash
Copy
Edit
voice-assistant/
├── main.py          # Main voice assistant script
├── otp.py           # Custom module for sending OTP (email functionality)
└── README.md        # Project documentation
🔧 Usage
Clone the repository:

bash
Copy
Edit
git clone https://github.com/your-username/voice-assistant.git
cd voice-assistant
Run the assistant:

bash
Copy
Edit
python main.py
Speak into your microphone and use commands like:

"How are you"

"Open web page"

"Send OTP"

"Open LinkedIn"

"Open GitHub"

"Shut down" to exit

✉️ OTP Module
Make sure you have the otp.py file in your directory. It should include a function otp(email) that handles email OTP sending logic using libraries like smtplib.

✅ To-Do
Add more voice commands (e.g., weather, news, jokes)

Improve error handling

Add GUI interface

📌 Disclaimer
This project is intended for educational purposes. Ensure you do not use your credentials or send sensitive information in production without proper security measures.

👨‍💻 Author
Your Name

Feel free to contribute or fork this project!

yaml
Copy
Edit
