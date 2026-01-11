import pdfplumber
import re
from typing import Dict, List, Optional
from io import BytesIO


class LinkedInPDFParser:
    """
    Parse LinkedIn profile PDF to extract:
    - Personal information
    - Work experience
    - Education
    - Skills
    - Certifications
    """
    
    def parse(self, pdf_content: bytes) -> Dict:
        """Parse LinkedIn PDF and return structured data"""
        try:
            with pdfplumber.open(BytesIO(pdf_content)) as pdf:
                text = ""
                for page in pdf.pages:
                    text += page.extract_text() + "\n"
            
            profile_data = {
                "name": self._extract_name(text),
                "headline": self._extract_headline(text),
                "experience": self._extract_experience(text),
                "education": self._extract_education(text),
                "skills": self._extract_skills(text),
                "certifications": self._extract_certifications(text),
            }
            
            return profile_data
            
        except Exception as e:
            print(f"PDF parsing error: {e}")
            return None
    
    def _extract_name(self, text: str) -> str:
        """Extract name from the first lines of the PDF"""
        lines = text.split('\n')
        # LinkedIn PDFs typically have the name in the first few lines
        for line in lines[:5]:
            if line.strip() and len(line.strip()) > 2:
                return line.strip()
        return "Unknown"
    
    def _extract_headline(self, text: str) -> str:
        """Extract professional headline"""
        lines = text.split('\n')
        # Usually appears after the name
        for i, line in enumerate(lines[:10]):
            if i > 0 and line.strip() and len(line.strip()) > 10:
                return line.strip()
        return ""
    
    def _extract_experience(self, text: str) -> List[Dict]:
        """Extract work experience section"""
        experiences = []
        
        # Look for "Experience" section
        experience_pattern = r'Experience\s+(.*?)(?=Education|Skills|Certifications|$)'
        match = re.search(experience_pattern, text, re.DOTALL | re.IGNORECASE)
        
        if match:
            experience_text = match.group(1)
            
            # Split by company/position patterns
            # LinkedIn format typically: Company Name\nPosition\nDates\nDescription
            entries = re.split(r'\n(?=[A-Z][a-z]+.*(?:Inc\.|LLC|Ltd|Corporation|Company))', experience_text)
            
            for entry in entries:
                if len(entry.strip()) > 20:  # Filter out noise
                    lines = entry.strip().split('\n')
                    experiences.append({
                        "company": lines[0] if len(lines) > 0 else "",
                        "position": lines[1] if len(lines) > 1 else "",
                        "duration": lines[2] if len(lines) > 2 else "",
                        "description": '\n'.join(lines[3:]) if len(lines) > 3 else ""
                    })
        
        return experiences
    
    def _extract_education(self, text: str) -> List[Dict]:
        """Extract education section"""
        education = []
        
        education_pattern = r'Education\s+(.*?)(?=Experience|Skills|Certifications|Licenses|$)'
        match = re.search(education_pattern, text, re.DOTALL | re.IGNORECASE)
        
        if match:
            edu_text = match.group(1)
            entries = edu_text.strip().split('\n\n')
            
            for entry in entries:
                if len(entry.strip()) > 10:
                    lines = entry.strip().split('\n')
                    education.append({
                        "institution": lines[0] if len(lines) > 0 else "",
                        "degree": lines[1] if len(lines) > 1 else "",
                        "duration": lines[2] if len(lines) > 2 else ""
                    })
        
        return education
    
    def _extract_skills(self, text: str) -> List[str]:
        """Extract skills section"""
        skills = []
        
        skills_pattern = r'Skills\s+(.*?)(?=Education|Experience|Certifications|Languages|$)'
        match = re.search(skills_pattern, text, re.DOTALL | re.IGNORECASE)
        
        if match:
            skills_text = match.group(1)
            # Split by newlines and bullet points
            skill_lines = re.split(r'[\n•·]', skills_text)
            skills = [s.strip() for s in skill_lines if s.strip() and len(s.strip()) < 50]
        
        return skills
    
    def _extract_certifications(self, text: str) -> List[Dict]:
        """Extract certifications and licenses"""
        certifications = []
        
        cert_pattern = r'(?:Certifications?|Licenses?)\s+(.*?)(?=Education|Experience|Skills|$)'
        match = re.search(cert_pattern, text, re.DOTALL | re.IGNORECASE)
        
        if match:
            cert_text = match.group(1)
            entries = cert_text.strip().split('\n\n')
            
            for entry in entries:
                if len(entry.strip()) > 5:
                    lines = entry.strip().split('\n')
                    certifications.append({
                        "name": lines[0] if len(lines) > 0 else "",
                        "issuer": lines[1] if len(lines) > 1 else "",
                        "date": lines[2] if len(lines) > 2 else ""
                    })
        
        return certifications
