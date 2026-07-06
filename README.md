# 🎯 Smart Meeting Assistant

An AI-powered meeting assistant that provides real-time transcription, meeting summaries, and voice-based Q&A using Gemini AI, Deepgram, and GetStream.

## 🚀 Features

- 🎙️ Real-time meeting transcription
- 🤖 AI-powered Q&A using "Hey Assistant"
- 📝 Automatic meeting summaries
- 🔊 Voice interaction with Gemini AI
- 📡 Live transcript streaming
- 👥 Multi-user meeting support
- ☁️ Cloud-based communication using GetStream

---

## 🛠️ Tech Stack

### Frontend
- Next.js
- React
- TypeScript
- Tailwind CSS

### Backend
- Python
- Vision Agents
- Gemini AI
- Deepgram Speech-to-Text
- GetStream Video SDK

### Tools
- Git
- GitHub
- VS Code

---

## 📂 Project Structure

```bash
Smart-Meeting-Assistant/
│
├── frontend/
│   ├── app/
│   ├── components/
│   ├── public/
│   └── package.json
│
├── backend/
│   ├── main.py
│   ├── requirements.txt
│   ├── .env
│   └── venv/
│
└── README.md
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/Smart-Meeting-Assistant.git
cd Smart-Meeting-Assistant
```

### Frontend Setup

```bash
cd frontend

npm install

npm run dev
```

Frontend runs on:

```bash
http://localhost:3000
```

### Backend Setup

```bash
cd backend

python -m venv venv

source venv/bin/activate

pip install -r requirements.txt

python main.py
```

---

## 🔑 Environment Variables

Create a `.env` file inside the backend folder.

```env
GOOGLE_API_KEY=YOUR_GEMINI_KEY

DEEPGRAM_API_KEY=YOUR_DEEPGRAM_KEY

STREAM_API_KEY=YOUR_STREAM_KEY

STREAM_API_SECRET=YOUR_STREAM_SECRET

CALL_ID=test-meeting
```

---

## 📋 Usage

1. Start backend server.
2. Start frontend application.
3. Open the meeting room.
4. Join using your name.
5. Speak normally for transcription.
6. Say:

```text
Hey Assistant
```

followed by a question.

Example:

```text
Hey Assistant, summarize today's discussion.
```

The AI assistant responds using the meeting context.

---

## 💡 Problem Statement

Remote meetings often require manual note-taking and post-meeting documentation. Important discussions can be missed, and participants may struggle to recall decisions made during the meeting.

---

## ✅ Solution

This project automatically transcribes meetings, generates summaries, and enables participants to ask contextual questions using natural language voice commands.

---

## 📈 Future Enhancements

- Meeting recording storage
- PDF summary export
- Email summary delivery
- Speaker identification
- Multi-language transcription
- Calendar integration

---

## 👨‍💻 Author

Ayan Thara

B.Tech Computer Science Engineering

GitHub: https://github.com/AyanThara

---

## ⭐ Resume Highlights

- Built an AI-powered meeting assistant using Gemini AI and Deepgram.
- Implemented real-time transcription and contextual Q&A.
- Integrated cloud-based meeting communication using GetStream.
- Developed full-stack architecture using Next.js and Python.
