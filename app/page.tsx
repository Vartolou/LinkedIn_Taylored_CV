'use client';

import { useState } from 'react';
import { useRouter } from 'next/navigation';
import { Briefcase, Linkedin, Mail, Lock } from 'lucide-react';

export default function Home() {
  const router = useRouter();
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [isSignUp, setIsSignUp] = useState(false);
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setLoading(true);

    try {
      // For MVP, simple auth - in production, use proper JWT
      const endpoint = isSignUp ? '/api/auth/signup' : '/api/auth/login';
      
      // Simulate auth for now
      setTimeout(() => {
        localStorage.setItem('user', JSON.stringify({ email }));
        router.push('/dashboard');
      }, 1000);
    } catch (error) {
      console.error('Auth error:', error);
      alert('Authentication failed. Please try again.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen flex items-center justify-center p-4">
      <div className="w-full max-w-6xl grid md:grid-cols-2 gap-8 items-center">
        {/* Left side - Branding */}
        <div className="text-center md:text-left space-y-6">
          <div className="flex items-center justify-center md:justify-start gap-3">
            <div className="bg-linkedin-500 p-3 rounded-xl">
              <Briefcase className="w-8 h-8" />
            </div>
            <h1 className="text-4xl font-bold">Li-Taylored CV</h1>
          </div>
          
          <h2 className="text-3xl md:text-4xl font-bold leading-tight">
            Your LinkedIn Profile,<br />
            <span className="text-linkedin-400">Perfectly Tailored</span><br />
            for Every Job
          </h2>
          
          <p className="text-gray-300 text-lg">
            Upload your LinkedIn PDF, paste a job description, and get an ATS-friendly CV and cover letter — without inventing skills.
          </p>
          
          <div className="flex flex-wrap gap-4 justify-center md:justify-start text-sm text-gray-400">
            <div className="flex items-center gap-2">
              <div className="w-2 h-2 bg-green-400 rounded-full"></div>
              <span>No fake experience</span>
            </div>
            <div className="flex items-center gap-2">
              <div className="w-2 h-2 bg-green-400 rounded-full"></div>
              <span>ATS-optimized</span>
            </div>
            <div className="flex items-center gap-2">
              <div className="w-2 h-2 bg-green-400 rounded-full"></div>
              <span>Match scoring</span>
            </div>
          </div>
        </div>

        {/* Right side - Auth Form */}
        <div className="glass-effect rounded-2xl p-8 space-y-6">
          <div className="text-center">
            <h3 className="text-2xl font-bold mb-2">
              {isSignUp ? 'Create Account' : 'Welcome Back'}
            </h3>
            <p className="text-gray-400">
              {isSignUp ? 'Start tailoring your applications' : 'Continue your job search'}
            </p>
          </div>

          <form onSubmit={handleSubmit} className="space-y-4">
            <div>
              <label className="block text-sm font-medium mb-2">Email</label>
              <div className="relative">
                <Mail className="absolute left-3 top-1/2 transform -translate-y-1/2 w-5 h-5 text-gray-400" />
                <input
                  type="email"
                  value={email}
                  onChange={(e) => setEmail(e.target.value)}
                  className="w-full bg-white/5 border border-white/10 rounded-lg py-3 pl-12 pr-4 focus:outline-none focus:border-linkedin-500 transition-colors"
                  placeholder="you@example.com"
                  required
                />
              </div>
            </div>

            <div>
              <label className="block text-sm font-medium mb-2">Password</label>
              <div className="relative">
                <Lock className="absolute left-3 top-1/2 transform -translate-y-1/2 w-5 h-5 text-gray-400" />
                <input
                  type="password"
                  value={password}
                  onChange={(e) => setPassword(e.target.value)}
                  className="w-full bg-white/5 border border-white/10 rounded-lg py-3 pl-12 pr-4 focus:outline-none focus:border-linkedin-500 transition-colors"
                  placeholder="••••••••"
                  required
                />
              </div>
            </div>

            <button
              type="submit"
              disabled={loading}
              className="w-full btn-primary"
            >
              {loading ? 'Processing...' : isSignUp ? 'Sign Up' : 'Sign In'}
            </button>
          </form>

          <div className="relative">
            <div className="absolute inset-0 flex items-center">
              <div className="w-full border-t border-white/10"></div>
            </div>
            <div className="relative flex justify-center text-sm">
              <span className="px-4 bg-linkedin-800 text-gray-400">or</span>
            </div>
          </div>

          <button className="w-full btn-secondary flex items-center justify-center gap-2">
            <Linkedin className="w-5 h-5" />
            Continue with LinkedIn
          </button>

          <div className="text-center text-sm">
            <button
              type="button"
              onClick={() => setIsSignUp(!isSignUp)}
              className="text-linkedin-400 hover:text-linkedin-300 transition-colors"
            >
              {isSignUp ? 'Already have an account? Sign in' : "Don't have an account? Sign up"}
            </button>
          </div>
        </div>
      </div>
    </div>
  );
}
