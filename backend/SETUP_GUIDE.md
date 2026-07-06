# Smart Meeting Assistant - Complete Setup Guide

## ✅ Issues Fixed

### 1. Backend Import Error ❌ → ✅
**Problem**: `ImportError: cannot import name 'CallSessionParticipantJoinedEvent'`
**Root Cause**: Code used vision-agents events that don't exist in v0.6.6
**Solution**: Updated code to use simpler, compatible event handling

### 2. Frontend "No tokens returned" ❌ → ✅
**Problem**: Frontend couldn't generate tokens
**Root Cause**: Missing `STREAM_API_KEY` and `STREAM_API_SECRET` in `.env`
**Solution**: Added to `.env` with detailed examples in `.env.example`

### 3. Missing Dependencies ❌ → ✅
**Solution**: Updated `requirements.txt` with correct versions

---

## 📋 Required API Keys (All Services)

### 1. **GetStream.io** (for video calls)
- **Where to Get**: https://getstream.io/try-for-free
- **What You Get**: `STREAM_API_KEY` and `STREAM_API_SECRET`
- **Why**: Powers real-time video calls and messaging

### 2. **Google Gemini API** (for AI responses)
- **Where to Get**: https://ai.google.dev
- **What You Get**: `GOOGLE_API_KEY`
- **Why**: Powers the AI assistant responses
- **Setup**: Enable Gemini API in Google Cloud

### 3. **Deepgram API** (for speech-to-text)
- **Where to Get**: https://console.deepgram.com
- **What You Get**: `DEEPGRAM_API_KEY`
- **Why**: Converts speech to text in real-time

---

## 🔧 Complete Setup Steps

### Step 1: Create `.env` File (Backend)

```bash
cd /Users/ayanthara/Desktop/Smart-Meeting-Assistant/backend
cp .env.example .env
```

### Step 2: Update `.env` with Your API Keys

Edit `.env`:

```env
# GetStream.io - Get from https://getstream.io/try-for-free
STREAM_API_KEY=your_actual_stream_api_key_here
STREAM_API_SECRET=your_actual_stream_api_secret_here

# Google Gemini - Get from https://ai.google.dev
GOOGLE_API_KEY=your_actual_gemini_api_key_here

# Deepgram - Get from https://console.deepgram.com
DEEPGRAM_API_KEY=your_actual_deepgram_api_key_here

# Meeting Config
CALL_ID=test-meeting
LOG_LEVEL=INFO
FRONTEND_URL=http://localhost:3000
```

### Step 3: Install Backend Dependencies

```bash
cd /Users/ayanthara/Desktop/Smart-Meeting-Assistant/backend

# Create and activate virtual environment (if not already done)
python3 -m venv venv
source venv/bin/activate

# Install latest dependencies
pip install --upgrade -r requirements.txt
```

### Step 4: Update Frontend Environment

The frontend needs `NEXT_PUBLIC_CALL_ID`:

```bash
cd /Users/ayanthara/Desktop/Smart-Meeting-Assistant/frontend

# Create .env.local if it doesn't exist
cat > .env.local << 'EOF'
NEXT_PUBLIC_CALL_ID=test-meeting
EOF
```

### Step 5: Install Frontend Dependencies

```bash
cd /Users/ayanthara/Desktop/Smart-Meeting-Assistant/frontend
npm install
```

---

## 🚀 Running the Project

### Terminal 1 - Backend (Python)

```bash
cd /Users/ayanthara/Desktop/Smart-Meeting-Assistant/backend

# Activate virtual environment
source venv/bin/activate

# Run the backend server
python main.py

# Or use the variant with auto-notes:
python main-alt.py
```

**Expected Output**:
```
🤖 Starting Meeting Assistant...
✅ Joining call...
================================
🎙️  MEETING ASSISTANT ACTIVE!
================================

Press Ctrl+C to stop
```

### Terminal 2 - Frontend (Node.js)

```bash
cd /Users/ayanthara/Desktop/Smart-Meeting-Assistant/frontend

# Run development server
npm run dev
```

**Expected Output**:
```
  ▲ Next.js 14.x.x
  - Local:        http://localhost:3000
  - Environments: .env.local
```

### Step 6: Test the Application

1. **Open Frontend**: http://localhost:3000
2. **Enter Username**: Type your name (or leave blank for "anonymous")
3. **Click "Join Meeting"**: Should now connect without "No tokens returned" error
4. **Speak in Meeting**: 
   - Say anything → Bot transcribes silently
   - Say "Hey Assistant, what did we discuss?" → Bot responds

---

## 📝 Available Versions

### `main.py` - Basic Transcription Mode
- Auto-transcription
- Q&A with "Hey Assistant"
- Real-time transcript streaming to frontend

### `main-alt.py` - Auto-Note Taking Mode
- Everything from main.py, PLUS:
- Automatic note generation
- Notes sent as JSON: `{"NOTES": "[note1, note2, ...]"}`
- Better context for Q&A

---

## ✅ Troubleshooting

### Backend: ImportError with vision_agents

**Error**: `ImportError: cannot import name 'X' from 'vision_agents.core.events'`

**Solution**:
```bash
# Update to latest version
pip install --upgrade 'vision-agents[getstream,gemini,deepgram]>=0.10.0'
```

### Frontend: "No tokens returned"

**Check**:
1. ✅ `.env` has `STREAM_API_KEY` and `STREAM_API_SECRET`
2. ✅ Keys are not the example values (YOUR_xxx)
3. ✅ Backend is running on same network
4. ✅ `.env.local` has `NEXT_PUBLIC_CALL_ID=test-meeting`

### Connection Issues

**Check**:
1. ✅ Both services running
2. ✅ Backend logs show "Joining call..."
3. ✅ Frontend shows "Connecting..." then loads
4. ✅ Internet connection is stable

### No transcription appears

**Check**:
1. ✅ Speaking clearly and loudly
2. ✅ Microphone is enabled in browser
3. ✅ Browser has permission to access mic
4. ✅ `DEEPGRAM_API_KEY` is valid

---

## 🔄 Environment Variable Reference

| Variable | Required | Source | Purpose |
|----------|----------|--------|---------|
| STREAM_API_KEY | ✅ Yes | GetStream.io | Video call authentication |
| STREAM_API_SECRET | ✅ Yes | GetStream.io | Video call authentication |
| GOOGLE_API_KEY | ✅ Yes | Google Cloud | Gemini AI responses |
| DEEPGRAM_API_KEY | ✅ Yes | Deepgram | Speech-to-text |
| CALL_ID | No | Any string | Meeting room ID |
| LOG_LEVEL | No | DEBUG/INFO/WARNING/ERROR | Logging verbosity |
| FRONTEND_URL | No | URL | Frontend origin (CORS) |
| NEXT_PUBLIC_CALL_ID | ✅ Yes (Frontend) | Any string | Meeting room ID |

---

## 📊 Project Structure

```
Smart-Meeting-Assistant/
├── backend/
│   ├── main.py           # ← Basic version (use this first)
│   ├── main-alt.py       # ← Advanced with notes
│   ├── requirements.txt   # ← Dependencies
│   ├── .env              # ← Your API keys (git ignored)
│   ├── .env.example      # ← Template
│   ├── SETUP_GUIDE.md    # ← You are here
│   └── venv/             # ← Virtual environment
│
└── frontend/
    ├── package.json      # ← Dependencies
    ├── .env.local        # ← Local config (git ignored)
    ├── app/
    │   ├── page.js       # ← Join page
    │   ├── meeting/      # ← Meeting room
    │   └── api/          # ← Token generation
    └── node_modules/
```

---

## 🆘 Quick Fixes

### Backend not starting?
```bash
# Make sure you're in the right directory
cd /Users/ayanthara/Desktop/Smart-Meeting-Assistant/backend

# Verify virtual environment is activated
source venv/bin/activate

# Clear pip cache and reinstall
pip cache purge
pip install --upgrade -r requirements.txt

# Try running again
python main.py
```

### Frontend stuck on "Connecting…"?
```bash
# Check if token API is working
curl -X POST http://localhost:3000/api/token \
  -H "Content-Type: application/json" \
  -d '{"userId": "test-user"}'

# Should return: {"token": "..."}
```

### Getting different errors?
1. ✅ Upgrade all dependencies: `pip install --upgrade -r requirements.txt`
2. ✅ Verify all API keys are set: `cat .env`
3. ✅ Clear node cache: `npm cache clean --force`
4. ✅ Check Node/Python versions

---

## 📚 Additional Resources

- **GetStream Documentation**: https://getstream.io/docs/
- **Vision Agents**: https://github.com/landing-ai/vision-agents
- **Next.js Docs**: https://nextjs.org/docs
- **Python async**: https://docs.python.org/3/library/asyncio.html

---

## 🎯 Next Steps

1. ✅ Get your API keys (15 minutes)
2. ✅ Update `.env` file
3. ✅ Run `pip install --upgrade -r requirements.txt`
4. ✅ Start backend: `python main.py`
5. ✅ Start frontend: `npm run dev`
6. ✅ Test: http://localhost:3000

**You're all set! 🚀**
