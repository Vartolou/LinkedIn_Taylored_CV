# Li-Taylored CV 🚀

**LinkedIn-Profile-Based Job Tailoring AI**

A modern web application that uses your LinkedIn profile (PDF) to intelligently tailor your CV and cover letter to any job description using AI — without inventing skills or experience.

![LinkedIn Theme](https://img.shields.io/badge/Theme-LinkedIn%20Blue-0A66C2)
![Tech Stack](https://img.shields.io/badge/Stack-Next.js%20%2B%20FastAPI-blue)
![AI Powered](https://img.shields.io/badge/AI-GPT--4-green)

## 🎯 Core Purpose

Use a user's LinkedIn profile (PDF) as a trusted source of experience and tailor CV + cover letter to a pasted job description. Nothing more. Nothing less.

## ✨ Features

### MVP Features (Essentials Only)

1. **User Authentication**
   - Email/password authentication
   - "Login with LinkedIn" (identity only, no data fetching)

2. **Import LinkedIn Profile**
   - Upload LinkedIn profile PDF
   - Simple instruction: "Download your LinkedIn profile as PDF (Profile → More → Save to PDF)"

3. **Job Description Input**
   - Simple textarea for pasting job specifications

4. **AI Processing** 🧠
   - Extracts experience + certifications from PDF
   - Extracts requirements + keywords from job spec
   - Matches & rewrites without inventing skills

5. **Outputs**
   - ✅ Tailored CV (PDF and DOCX)
   - ✅ Tailored Cover Letter (PDF and DOCX)
   - ✅ Match Score with missing skills analysis

## 🛡️ Ethical AI Principles

### What the AI CAN do:
- ✔ Rephrase existing experience
- ✔ Emphasize relevant skills
- ✔ Reorder content strategically
- ✔ Translate experience into job-specific language

### What the AI CANNOT do:
- ❌ Invent skills you don't have
- ❌ Add fake experience
- ❌ Fabricate certifications

**This is your ethical differentiator.**

## 🖥️ User Flow

```
Login
  ↓
Upload LinkedIn PDF
  ↓
Paste Job Description
  ↓
Click "Tailor My Application"
  ↓
Download CV + Cover Letter
```

## 🏗️ Tech Stack

### Frontend
- **Next.js 14** - React framework with App Router
- **TypeScript** - Type safety
- **Tailwind CSS** - Styling with custom LinkedIn theme
- **Lucide React** - Modern icons

### Backend
- **FastAPI** - High-performance Python API
- **pdfplumber** - PDF text extraction
- **OpenAI GPT-4** - AI processing and content generation
- **ReportLab** - PDF generation
- **python-docx** - DOCX generation

### AI Pipeline
- LLM-based prompt engineering
- Semantic matching for skill analysis
- ATS-friendly formatting

## 📦 Installation

### Prerequisites
- Node.js 18+ and npm
- Python 3.9+
- OpenAI API key

### 1. Clone the repository
```bash
git clone <repository-url>
cd Li_Taylored_CV
```

### 2. Frontend Setup
```bash
npm install
```

### 3. Backend Setup
```bash
cd backend
pip install -r requirements.txt
```

### 4. Environment Variables

Create a `.env` file in the `backend` directory:

```env
OPENAI_API_KEY=your_openai_api_key_here
```

## 🚀 Running the Application

### Start the Backend (Terminal 1)
```bash
cd backend
python main.py
```
The API will run on `http://localhost:8000`

### Start the Frontend (Terminal 2)
```bash
npm run dev
```
The app will run on `http://localhost:3000`

### Access the Application
Open your browser and navigate to `http://localhost:3000`

## 📂 Project Structure

```
Li_Taylored_CV/
├── app/                      # Next.js app directory
│   ├── page.tsx             # Login page
│   ├── dashboard/           
│   │   └── page.tsx         # Main application flow
│   ├── layout.tsx           # Root layout
│   └── globals.css          # Global styles with LinkedIn theme
├── backend/
│   ├── main.py              # FastAPI application
│   ├── services/
│   │   ├── pdf_parser.py    # LinkedIn PDF parsing
│   │   ├── ai_processor.py  # AI tailoring logic
│   │   └── document_generator.py  # PDF/DOCX generation
│   ├── requirements.txt     # Python dependencies
│   └── temp/                # Generated documents
├── package.json             # Node.js dependencies
├── tailwind.config.js       # Tailwind configuration
├── tsconfig.json            # TypeScript configuration
└── README.md
```

## 📊 Data Model

```json
{
  "experience": [...],
  "certifications": [...],
  "job_requirements": [...],
  "match_score": 0.74,
  "missing_skills": ["Docker", "AWS"]
}
```

## 🎨 Design System

### Color Palette (LinkedIn Theme)
- **Primary Blue**: `#0a66c2` (LinkedIn brand color)
- **Dark Background**: `#001d3d` to `#000f21` (gradient)
- **Accent Colors**: Various shades of LinkedIn blue

### UI Components
- Glass-morphism effects
- Smooth transitions and hover states
- Modern, professional design
- Fully responsive layout

## 🧪 MVP Scope

### INCLUDED ✅
- CV tailoring
- Cover letter generation
- Match score calculation
- PDF/DOCX downloads

### EXCLUDED (Future Enhancements) ❌
- Auto-apply to jobs
- Resume builder UI
- Skill learning paths
- Multi-language support
- Analytics dashboard
- Job tracking
- Interview preparation

## 🎓 Academic Presentation

**How to describe this project:**

> "This system uses user-provided LinkedIn exports as a verified data source and applies NLP techniques to safely tailor job applications without hallucinating experience. The AI pipeline emphasizes semantic matching and ethical content rephrasing to optimize applications for ATS systems while maintaining factual accuracy."

**Key Technical Highlights:**
- PDF parsing and structured data extraction
- Prompt engineering for ethical AI constraints
- Semantic similarity matching for skill analysis
- ATS-optimized document generation
- RESTful API design with FastAPI
- Modern React architecture with Next.js

## 🔐 Security Notes

- For MVP: Simple authentication (upgrade to JWT for production)
- API keys stored in environment variables
- No LinkedIn API usage (GDPR-friendly)
- User data processed on-demand, not stored

## 🤝 Contributing

This is an MVP project. Future enhancements welcome:
- Enhanced PDF parsing for various LinkedIn formats
- Multiple LLM provider support
- Advanced ATS scoring
- Real-time collaboration features
- Job tracking and application management

## 📝 License

MIT License - Feel free to use for academic and personal projects.

## 🙏 Acknowledgments

- Built with ethical AI principles at the core
- Designed for students and job seekers
- Academic project demonstrating practical AI application

## 📧 Support

For issues or questions, please open an issue in the repository.

---

**Made with 💙 using LinkedIn's color palette and modern web technologies**
