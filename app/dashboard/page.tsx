'use client';

import { useState, useEffect } from 'react';
import { useRouter } from 'next/navigation';
import { Upload, FileText, Sparkles, Download, LogOut, AlertCircle } from 'lucide-react';
import axios from 'axios';

export default function Dashboard() {
  const router = useRouter();
  const [step, setStep] = useState(1);
  const [pdfFile, setPdfFile] = useState<File | null>(null);
  const [jobDescription, setJobDescription] = useState('');
  const [loading, setLoading] = useState(false);
  const [results, setResults] = useState<any>(null);

  useEffect(() => {
    const user = localStorage.getItem('user');
    if (!user) {
      router.push('/');
    }
  }, [router]);

  const handleLogout = () => {
    localStorage.removeItem('user');
    router.push('/');
  };

  const handlePdfUpload = (e: React.ChangeEvent<HTMLInputElement>) => {
    if (e.target.files && e.target.files[0]) {
      setPdfFile(e.target.files[0]);
    }
  };

  const handleTailorApplication = async () => {
    if (!pdfFile || !jobDescription) {
      alert('Please upload your LinkedIn PDF and paste the job description');
      return;
    }

    setLoading(true);

    try {
      const formData = new FormData();
      formData.append('linkedin_pdf', pdfFile);
      formData.append('job_description', jobDescription);

      const response = await axios.post('http://localhost:8000/tailor', formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
      });

      setResults(response.data);
      setStep(3);
    } catch (error) {
      console.error('Error:', error);
      alert('Failed to process application. Please try again.');
    } finally {
      setLoading(false);
    }
  };

  const downloadDocument = async (type: 'cv' | 'cover_letter') => {
    try {
      const response = await axios.get(`http://localhost:8000/download/${type}`, {
        responseType: 'blob',
      });

      const url = window.URL.createObjectURL(new Blob([response.data]));
      const link = document.createElement('a');
      link.href = url;
      link.setAttribute('download', `${type === 'cv' ? 'tailored_cv' : 'cover_letter'}.pdf`);
      document.body.appendChild(link);
      link.click();
      link.remove();
    } catch (error) {
      console.error('Download error:', error);
      alert('Failed to download document');
    }
  };

  return (
    <div className="min-h-screen p-4 md:p-8">
      {/* Header */}
      <div className="max-w-6xl mx-auto mb-8">
        <div className="flex justify-between items-center glass-effect rounded-xl p-4">
          <div className="flex items-center gap-3">
            <div className="bg-linkedin-500 p-2 rounded-lg">
              <FileText className="w-6 h-6" />
            </div>
            <h1 className="text-2xl font-bold">Li-Taylored CV</h1>
          </div>
          <button
            onClick={handleLogout}
            className="flex items-center gap-2 text-gray-400 hover:text-white transition-colors"
          >
            <LogOut className="w-5 h-5" />
            <span>Logout</span>
          </button>
        </div>
      </div>

      {/* Main Content */}
      <div className="max-w-6xl mx-auto">
        {/* Progress Steps */}
        <div className="flex justify-center mb-12">
          <div className="flex items-center gap-4">
            {[1, 2, 3].map((s) => (
              <div key={s} className="flex items-center gap-4">
                <div
                  className={`w-12 h-12 rounded-full flex items-center justify-center font-bold transition-all ${
                    step >= s ? 'bg-linkedin-500' : 'glass-effect'
                  }`}
                >
                  {s}
                </div>
                {s < 3 && (
                  <div
                    className={`w-24 h-1 rounded ${
                      step > s ? 'bg-linkedin-500' : 'bg-white/10'
                    }`}
                  ></div>
                )}
              </div>
            ))}
          </div>
        </div>

        {/* Step 1: Upload LinkedIn PDF */}
        {step === 1 && (
          <div className="glass-effect rounded-2xl p-8 max-w-2xl mx-auto space-y-6">
            <div className="text-center space-y-2">
              <Upload className="w-16 h-16 mx-auto text-linkedin-400" />
              <h2 className="text-3xl font-bold">Upload Your LinkedIn Profile</h2>
              <p className="text-gray-400">
                Download your LinkedIn profile as PDF (Profile → More → Save to PDF)
              </p>
            </div>

            <div className="border-2 border-dashed border-white/20 rounded-xl p-12 text-center hover:border-linkedin-500 transition-colors cursor-pointer">
              <input
                type="file"
                accept=".pdf"
                onChange={handlePdfUpload}
                className="hidden"
                id="pdf-upload"
              />
              <label htmlFor="pdf-upload" className="cursor-pointer">
                {pdfFile ? (
                  <div className="space-y-2">
                    <FileText className="w-12 h-12 mx-auto text-green-400" />
                    <p className="font-medium">{pdfFile.name}</p>
                    <p className="text-sm text-gray-400">Click to change</p>
                  </div>
                ) : (
                  <div className="space-y-2">
                    <Upload className="w-12 h-12 mx-auto text-gray-400" />
                    <p className="font-medium">Click to upload or drag and drop</p>
                    <p className="text-sm text-gray-400">PDF files only</p>
                  </div>
                )}
              </label>
            </div>

            <button
              onClick={() => pdfFile && setStep(2)}
              disabled={!pdfFile}
              className="w-full btn-primary disabled:opacity-50 disabled:cursor-not-allowed"
            >
              Continue to Job Description
            </button>
          </div>
        )}

        {/* Step 2: Paste Job Description */}
        {step === 2 && (
          <div className="glass-effect rounded-2xl p-8 max-w-4xl mx-auto space-y-6">
            <div className="text-center space-y-2">
              <FileText className="w-16 h-16 mx-auto text-linkedin-400" />
              <h2 className="text-3xl font-bold">Paste the Job Description</h2>
              <p className="text-gray-400">
                Copy and paste the complete job posting from any source
              </p>
            </div>

            <textarea
              value={jobDescription}
              onChange={(e) => setJobDescription(e.target.value)}
              className="w-full h-96 bg-white/5 border border-white/10 rounded-lg p-4 focus:outline-none focus:border-linkedin-500 transition-colors resize-none"
              placeholder="Paste the job description here including:
- Job title
- Required skills
- Experience requirements
- Responsibilities
- Qualifications..."
            />

            <div className="flex gap-4">
              <button onClick={() => setStep(1)} className="flex-1 btn-secondary">
                Back
              </button>
              <button
                onClick={handleTailorApplication}
                disabled={!jobDescription || loading}
                className="flex-1 btn-primary disabled:opacity-50 disabled:cursor-not-allowed flex items-center justify-center gap-2"
              >
                {loading ? (
                  <>Processing...</>
                ) : (
                  <>
                    <Sparkles className="w-5 h-5" />
                    Tailor My Application
                  </>
                )}
              </button>
            </div>
          </div>
        )}

        {/* Step 3: Results */}
        {step === 3 && results && (
          <div className="space-y-6">
            {/* Match Score */}
            <div className="glass-effect rounded-2xl p-8 max-w-2xl mx-auto text-center">
              <h2 className="text-2xl font-bold mb-4">Match Analysis</h2>
              <div className="mb-6">
                <div className="text-6xl font-bold text-linkedin-400 mb-2">
                  {results.match_score}%
                </div>
                <p className="text-gray-400">Match Score</p>
              </div>
              
              {results.missing_skills && results.missing_skills.length > 0 && (
                <div className="bg-yellow-500/10 border border-yellow-500/20 rounded-lg p-4">
                  <div className="flex items-start gap-2">
                    <AlertCircle className="w-5 h-5 text-yellow-400 flex-shrink-0 mt-0.5" />
                    <div className="text-left">
                      <p className="font-medium text-yellow-400 mb-2">Missing Skills:</p>
                      <p className="text-sm text-gray-300">
                        {results.missing_skills.join(', ')}
                      </p>
                    </div>
                  </div>
                </div>
              )}
            </div>

            {/* Download Options */}
            <div className="grid md:grid-cols-2 gap-6 max-w-4xl mx-auto">
              <div className="glass-effect rounded-2xl p-8 space-y-4">
                <div className="bg-linkedin-500/20 w-16 h-16 rounded-xl flex items-center justify-center mb-4">
                  <FileText className="w-8 h-8 text-linkedin-400" />
                </div>
                <h3 className="text-2xl font-bold">Tailored CV</h3>
                <p className="text-gray-400">
                  ATS-friendly resume emphasizing relevant experience
                </p>
                <button
                  onClick={() => downloadDocument('cv')}
                  className="w-full btn-primary flex items-center justify-center gap-2"
                >
                  <Download className="w-5 h-5" />
                  Download CV
                </button>
              </div>

              <div className="glass-effect rounded-2xl p-8 space-y-4">
                <div className="bg-linkedin-500/20 w-16 h-16 rounded-xl flex items-center justify-center mb-4">
                  <FileText className="w-8 h-8 text-linkedin-400" />
                </div>
                <h3 className="text-2xl font-bold">Cover Letter</h3>
                <p className="text-gray-400">
                  Personalized letter based on your LinkedIn profile
                </p>
                <button
                  onClick={() => downloadDocument('cover_letter')}
                  className="w-full btn-primary flex items-center justify-center gap-2"
                >
                  <Download className="w-5 h-5" />
                  Download Cover Letter
                </button>
              </div>
            </div>

            {/* Start Over Button */}
            <div className="text-center">
              <button
                onClick={() => {
                  setStep(1);
                  setPdfFile(null);
                  setJobDescription('');
                  setResults(null);
                }}
                className="btn-secondary"
              >
                Tailor Another Application
              </button>
            </div>
          </div>
        )}
      </div>
    </div>
  );
}
