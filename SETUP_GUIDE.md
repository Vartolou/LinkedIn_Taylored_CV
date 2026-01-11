# 🚀 Quick Start Guide for Li-Taylored CV

## Step-by-Step Setup Instructions

### Prerequisites Check
Before starting, make sure you have:
- ✅ Node.js (version 18 or higher) - [Download here](https://nodejs.org/)
- ✅ Python (version 3.9 or higher) - [Download here](https://www.python.org/downloads/)
- ✅ OpenAI API Key - [Get one here](https://platform.openai.com/api-keys)

---

## 🔧 Installation Steps

### Step 1: Install Frontend Dependencies

Open a terminal in the project root directory and run:

```bash
npm install
```

This will install all the Next.js, React, and TypeScript dependencies.

**Expected output:** You should see packages being downloaded and installed.

---

### Step 2: Install Backend Dependencies

Navigate to the backend directory and install Python packages:

```bash
cd backend
pip install -r requirements.txt
```

Or if you're using Python 3 specifically:

```bash
pip3 install -r requirements.txt
```

**Expected output:** All Python packages (FastAPI, pdfplumber, OpenAI, etc.) will be installed.

---

### Step 3: Set Up Environment Variables

1. In the `backend` folder, create a new file called `.env` (copy from `.env.example`):

```bash
# Windows Command Prompt
copy .env.example .env

# Windows PowerShell
Copy-Item .env.example .env

# Mac/Linux
cp .env.example .env
```

2. Open the `.env` file and add your OpenAI API key:

```env
OPENAI_API_KEY=sk-your-actual-api-key-here
CORS_ORIGINS=http://localhost:3000
DEBUG=True
```

**Where to get your OpenAI API Key:**
- Go to https://platform.openai.com/api-keys
- Create a new secret key
- Copy and paste it into the `.env` file

---

## ▶️ Running the Application

You have **two options** to run the application:

### Option 1: Automatic Start (Easiest) 🎯

**For Windows:**
Double-click the `start.bat` file in the project root.

**For Mac/Linux:**
```bash
bash start.sh
```

This will automatically start both the backend and frontend servers in separate windows.

---

### Option 2: Manual Start (More Control) 🎮

**Terminal 1 - Start the Backend:**
```bash
cd backend
python main.py
```

You should see:
```
INFO:     Started server process
INFO:     Uvicorn running on http://0.0.0.0:8000
```

**Terminal 2 - Start the Frontend (keep Terminal 1 running):**

Open a new terminal in the project root and run:
```bash
npm run dev
```

You should see:
```
▲ Next.js 14.0.4
- Local:        http://localhost:3000
```

---

## 🌐 Access the Application

1. **Open your web browser**
2. **Navigate to:** http://localhost:3000
3. **You should see the Li-Taylored CV login page with the dark blue LinkedIn theme**

---

## 🧪 Testing the Application

### Quick Test Flow:

1. **Create an account** or sign in (for MVP, any email/password works)
2. **Prepare a LinkedIn PDF:**
   - Go to your LinkedIn profile
   - Click "More" → "Save to PDF"
   - Download the PDF

3. **Upload the PDF** on the dashboard
4. **Paste a job description** (copy from any job posting)
5. **Click "Tailor My Application"**
6. **View results** and download your tailored CV and cover letter

---

## 🔍 Troubleshooting

### Problem: "Port 3000 is already in use"
**Solution:** Stop any other Next.js apps running, or use a different port:
```bash
npm run dev -- -p 3001
```

### Problem: "Port 8000 is already in use"
**Solution:** Stop any other Python servers, or change the port in `backend/main.py`:
```python
uvicorn.run(app, host="0.0.0.0", port=8001)
```
Also update `next.config.js` to match the new port.

### Problem: "OpenAI API error"
**Solution:** 
- Check your `.env` file has the correct API key
- Verify your OpenAI account has credits
- Make sure the key starts with `sk-`

### Problem: "Module not found" errors
**Solution:**
```bash
# Frontend
npm install

# Backend
cd backend
pip install -r requirements.txt --upgrade
```

### Problem: Backend not connecting to frontend
**Solution:**
- Make sure both servers are running
- Check the backend is on http://localhost:8000
- Check CORS settings in `backend/main.py`
- Clear browser cache and refresh

---

## 📦 Development Mode Features

### Backend API Documentation
Once the backend is running, visit:
- **Interactive API Docs:** http://localhost:8000/docs
- **Alternative Docs:** http://localhost:8000/redoc

### Hot Reload
Both servers support hot reload:
- **Frontend:** Changes to `.tsx` files automatically refresh
- **Backend:** Uvicorn watches for Python file changes

---

## 🎯 What Happens Behind the Scenes

1. **PDF Upload** → Backend extracts text using pdfplumber
2. **Job Description** → AI analyzes requirements and keywords
3. **Matching** → Compares your skills with job requirements
4. **Tailoring** → GPT-4 rephrases your experience (ethically)
5. **Generation** → Creates ATS-friendly PDF and DOCX files
6. **Download** → You get tailored documents ready to apply!

---

## 📊 System Check Commands

### Check Node.js version:
```bash
node --version
# Should show v18.x.x or higher
```

### Check Python version:
```bash
python --version
# Should show 3.9.x or higher
```

### Check if ports are available:
```bash
# Windows
netstat -ano | findstr :3000
netstat -ano | findstr :8000

# Mac/Linux
lsof -i :3000
lsof -i :8000
```

---

## 🆘 Still Having Issues?

1. **Make sure all dependencies are installed correctly**
2. **Check your `.env` file has the OpenAI API key**
3. **Verify both servers are running without errors**
4. **Check browser console for frontend errors (F12)**
5. **Check terminal output for backend errors**

---

## 📝 Quick Reference

| Component | URL | Purpose |
|-----------|-----|---------|
| Frontend | http://localhost:3000 | User interface |
| Backend API | http://localhost:8000 | API server |
| API Docs | http://localhost:8000/docs | Interactive API documentation |

---

## ✅ Success Checklist

- [ ] Node.js and Python installed
- [ ] Frontend dependencies installed (`npm install`)
- [ ] Backend dependencies installed (`pip install -r requirements.txt`)
- [ ] `.env` file created with OpenAI API key
- [ ] Backend running on port 8000
- [ ] Frontend running on port 3000
- [ ] Application loads in browser
- [ ] Can upload PDF and paste job description

---

**You're all set! Happy job hunting! 🎉**
