from fastapi import FastAPI, UploadFile, File, Form, HTTPException
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
import os
import json
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

from services.pdf_parser import LinkedInPDFParser
from services.ai_processor import AIProcessor
from services.document_generator import DocumentGenerator

app = FastAPI(title="Li-Taylored CV API")

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize services
pdf_parser = LinkedInPDFParser()
ai_processor = AIProcessor()
doc_generator = DocumentGenerator()

# Create temp directory for storing generated files
os.makedirs("temp", exist_ok=True)


class AuthRequest(BaseModel):
    email: str
    password: str


class TailorResponse(BaseModel):
    match_score: int
    missing_skills: List[str]
    cv_path: str
    cover_letter_path: str


@app.get("/")
async def root():
    return {"message": "Li-Taylored CV API", "status": "running"}


@app.post("/auth/signup")
async def signup(auth: AuthRequest):
    """MVP: Simple authentication - in production, use proper JWT and database"""
    # For MVP, just return success
    return {"message": "Account created successfully", "email": auth.email}


@app.post("/auth/login")
async def login(auth: AuthRequest):
    """MVP: Simple authentication - in production, use proper JWT"""
    # For MVP, just return success
    return {"message": "Login successful", "email": auth.email, "token": "mock_token"}


@app.post("/tailor", response_model=TailorResponse)
async def tailor_application(
    linkedin_pdf: UploadFile = File(...),
    job_description: str = Form(...)
):
    """
    Main endpoint: Parse LinkedIn PDF, analyze job description,
    and generate tailored CV and cover letter
    """
    try:
        # 1. Parse LinkedIn PDF
        print(f"Parsing PDF: {linkedin_pdf.filename}")
        pdf_content = await linkedin_pdf.read()
        profile_data = pdf_parser.parse(pdf_content)
        
        if not profile_data:
            raise HTTPException(status_code=400, detail="Failed to parse LinkedIn PDF")
        
        print(f"Profile parsed: {profile_data.get('name', 'Unknown')}")
        
        # 2. Process with AI
        print("Processing with AI...")
        ai_result = ai_processor.process(profile_data, job_description)
        
        print(f"Match score: {ai_result['match_score']}%")
        
        # 3. Generate documents
        print("Generating documents...")
        cv_path = doc_generator.generate_cv(ai_result)
        cover_letter_path = doc_generator.generate_cover_letter(ai_result)
        
        print("Documents generated successfully")
        
        return TailorResponse(
            match_score=ai_result["match_score"],
            missing_skills=ai_result["missing_skills"],
            cv_path=cv_path,
            cover_letter_path=cover_letter_path
        )
        
    except Exception as e:
        import traceback
        print(f"ERROR: {str(e)}")
        print(traceback.format_exc())
        raise HTTPException(status_code=500, detail=f"Processing error: {str(e)}")


@app.get("/download/{doc_type}")
async def download_document(doc_type: str):
    """Download generated CV or cover letter"""
    if doc_type not in ["cv", "cover_letter"]:
        raise HTTPException(status_code=400, detail="Invalid document type")
    
    file_path = f"temp/{doc_type}.pdf"
    
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="Document not found")
    
    return FileResponse(
        file_path,
        media_type="application/pdf",
        filename=f"tailored_{doc_type}.pdf"
    )


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
