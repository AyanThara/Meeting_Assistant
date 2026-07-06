# Quick Commands Reference

## 🚀 QUICKSTART (Copy & Paste)

### Setup (one-time)
```bash
# Backend setup
cd ~/Desktop/Smart-Meeting-Assistant/backend
python3 -m venv venv
source venv/bin/activate
pip install --upgrade -r requirements.txt
cp .env.example .env
# ↓ EDIT .env with your API keys ↓

# Frontend setup
cd ~/Desktop/Smart-Meeting-Assistant/frontend
npm install
cp .env.example .env.local
```

### Run (every time)
```bash
# Terminal 1 - Backend
cd ~/Desktop/Smart-Meeting-Assistant/backend
source venv/bin/activate
python main.py

# Terminal 2 - Frontend
cd ~/Desktop/Smart-Meeting-Assistant/frontend
npm run dev
```

## ✅ What to expect

Backend starts:
```
🤖 Starting Meeting Assistant...
✅ Joining call...
🎙️  MEETING ASSISTANT ACTIVE!
```

Frontend starts:
```
▲ Next.js
  - Local: http://localhost:3000
```

Open http://localhost:3000 and join a meeting

## 🔗 API Key Links
- GetStream: https://getstream.io/try-for-free
- Gemini: https://ai.google.dev
- Deepgram: https://console.deepgram.com

## 📝 Need API Keys?
1. Go to GetStream: https://getstream.io/try-for-free → Sign up → Get keys
2. Go to Google AI: https://ai.google.dev → Create API key
3. Go to Deepgram: https://console.deepgram.com → Sign up → Get keys
4. Put them in backend/.env

## 🆘 Common Issues

No tokens returned?
→ Check backend/.env has STREAM_API_KEY and STREAM_API_SECRET

Backend won't start?
→ pip install --upgrade -r requirements.txt

Frontend won't connect?
→ Make sure backend is running on same network

Still stuck?
→ Check SETUP_GUIDE.md for detailed troubleshooting
