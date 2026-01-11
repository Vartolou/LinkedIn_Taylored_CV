import os
import re
from typing import Dict, List
from anthropic import Anthropic
import json


class AIProcessor:
    """
    AI processor for:
    1. Analyzing job requirements
    2. Matching profile to job
    3. Tailoring CV content
    4. Generating cover letter
    
    ETHICAL RULES:
    - Only rephrase existing experience
    - Never invent skills or experience
    - Highlight relevant parts
    - Use job-specific language
    """
    
    def __init__(self):
        api_key = os.getenv("ANTHROPIC_API_KEY")
        if not api_key:
            print("Warning: ANTHROPIC_API_KEY not set. Using mock mode.")
            self.client = None
        else:
            self.client = Anthropic(api_key=api_key)
    
    def process(self, profile_data: Dict, job_description: str) -> Dict:
        """Main processing pipeline"""
        
        # Extract job requirements
        job_requirements = self._extract_job_requirements(job_description)
        
        # Calculate match score
        match_result = self._calculate_match(profile_data, job_requirements)
        
        # Tailor CV content
        tailored_content = self._tailor_content(profile_data, job_description, job_requirements)
        
        # Generate cover letter
        cover_letter = self._generate_cover_letter(profile_data, job_description)
        
        return {
            "profile_data": profile_data,
            "job_description": job_description,
            "job_requirements": job_requirements,
            "match_score": match_result["score"],
            "missing_skills": match_result["missing"],
            "tailored_experience": tailored_content["experience"],
            "tailored_skills": tailored_content["skills"],
            "cover_letter": cover_letter,
        }
    
    def _extract_job_requirements(self, job_description: str) -> Dict:
        """Extract key requirements from job description"""
        
        if not self.client:
            # Mock mode - extract basic keywords from job description
            skills = []
            common_skills = ["python", "javascript", "react", "sql", "docker", "aws", "java", "c++", "typescript", 
                           "nodejs", "database", "api", "agile", "git", "testing", "communication", "teamwork"]
            
            job_lower = job_description.lower()
            for skill in common_skills:
                if skill in job_lower:
                    skills.append(skill.title())
            
            return {
                "required_skills": skills[:5] if skills else ["Communication", "Teamwork"],
                "preferred_skills": skills[5:8] if len(skills) > 5 else [],
                "experience_years": "2-5 years",
                "key_responsibilities": ["Perform job duties", "Work with team"]
            }
        
        prompt = f"""
        Analyze this job description and extract:
        1. Required skills (must-have)
        2. Preferred skills (nice-to-have)
        3. Years of experience required
        4. Key responsibilities
        
        Job Description:
        {job_description}
        
        Return as JSON with keys: required_skills, preferred_skills, experience_years, key_responsibilities
        """
        
        try:
            response = self.client.messages.create(
                model="claude-3-5-sonnet-20241022",
                max_tokens=2048,
                temperature=0.3,
                system="You are a job requirement analyzer. Extract key information and return valid JSON.",
                messages=[
                    {"role": "user", "content": prompt}
                ]
            )
            
            return json.loads(response.content[0].text)
        except Exception as e:
            print(f"AI extraction error: {e}")
            return {"required_skills": [], "preferred_skills": [], "experience_years": "", "key_responsibilities": []}
    
    def _calculate_match(self, profile_data: Dict, job_requirements: Dict) -> Dict:
        """Calculate match score between profile and job requirements"""
        
        profile_skills = set([s.lower() for s in profile_data.get("skills", [])])
        required_skills = set([s.lower() for s in job_requirements.get("required_skills", [])])
        preferred_skills = set([s.lower() for s in job_requirements.get("preferred_skills", [])])
        
        # Check matches
        matched_required = profile_skills & required_skills
        matched_preferred = profile_skills & preferred_skills
        missing_required = required_skills - profile_skills
        
        # Calculate score (70% required, 30% preferred)
        required_score = (len(matched_required) / len(required_skills) * 70) if required_skills else 70
        preferred_score = (len(matched_preferred) / len(preferred_skills) * 30) if preferred_skills else 30
        
        total_score = int(required_score + preferred_score)
        
        # Ensure reasonable score (at least 40%)
        if total_score < 40:
            total_score = 40 + (total_score // 2)
        
        return {
            "score": min(total_score, 95),  # Cap at 95%
            "missing": list(missing_required)[:5]  # Limit to 5 missing skills
        }
    
    def _tailor_content(self, profile_data: Dict, job_description: str, job_requirements: Dict) -> Dict:
        """Tailor CV content to match job requirements"""
        
        if not self.client:
            # Mock mode - return original data
            return {
                "experience": profile_data.get("experience", []),
                "skills": profile_data.get("skills", [])
            }
        
        prompt = f"""
        CRITICAL ETHICAL RULES:
        - ONLY use experience from the profile
        - NEVER invent skills or experience
        - Rephrase and emphasize relevant parts
        - Use keywords from job description
        
        Profile Experience:
        {profile_data.get('experience', [])}
        
        Profile Skills:
        {profile_data.get('skills', [])}
        
        Job Requirements:
        {job_requirements}
        
        Tailor the experience descriptions to emphasize relevant skills and use job-specific language.
        Reorder skills to put the most relevant ones first.
        
        Return JSON with keys: experience (array), skills (array)
        """
        
        try:
            response = self.client.messages.create(
                model="claude-3-5-sonnet-20241022",
                max_tokens=4096,
                temperature=0.5,
                system="You are a CV tailoring expert. Emphasize relevant experience without inventing content.",
                messages=[
                    {"role": "user", "content": prompt}
                ]
            )
            
            return json.loads(response.content[0].text)
        except Exception as e:
            print(f"AI tailoring error: {e}")
            return {"experience": profile_data.get("experience", []), "skills": profile_data.get("skills", [])}
    
    def _generate_cover_letter(self, profile_data: Dict, job_description: str) -> str:
        """Generate personalized cover letter"""
        
        if not self.client:
            # Mock mode
            return f"""Dear Hiring Manager,

I am writing to express my strong interest in the position as described in your job posting.

With my background in {', '.join(profile_data.get('skills', [])[:3])}, I am confident in my ability to contribute to your team.

{profile_data.get('experience', [{}])[0].get('description', 'My experience includes relevant work in the field.')}

I look forward to discussing how my skills and experience align with your needs.

Best regards,
{profile_data.get('name', 'Applicant')}"""
        
        prompt = f"""
        Write a professional cover letter based ONLY on this LinkedIn profile.
        
        Profile:
        Name: {profile_data.get('name', '')}
        Headline: {profile_data.get('headline', '')}
        Experience: {profile_data.get('experience', [])}
        Skills: {profile_data.get('skills', [])}
        
        Job Description:
        {job_description}
        
        RULES:
        - Use only information from the profile
        - Match the tone to the job description
        - Highlight relevant experience
        - Keep it concise (3-4 paragraphs)
        - Be genuine and professional
        """
        
        try:
            response = self.client.messages.create(
                model="claude-3-5-sonnet-20241022",
                max_tokens=2048,
                temperature=0.7,
                system="You are a professional cover letter writer. Use only provided information.",
                messages=[
                    {"role": "user", "content": prompt}
                ]
            )
            
            return response.content[0].text
        except Exception as e:
            print(f"AI cover letter error: {e}")
            return "Error generating cover letter"
