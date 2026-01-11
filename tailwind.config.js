/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './pages/**/*.{js,ts,jsx,tsx,mdx}',
    './components/**/*.{js,ts,jsx,tsx,mdx}',
    './app/**/*.{js,ts,jsx,tsx,mdx}',
  ],
  theme: {
    extend: {
      colors: {
        linkedin: {
          50: '#e7f3ff',
          100: '#c7e0ff',
          200: '#94c7ff',
          300: '#5ba4ff',
          400: '#2e86ff',
          500: '#0a66c2', // Primary LinkedIn blue
          600: '#004182',
          700: '#002e5f',
          800: '#001d3d',
          900: '#000f21',
        },
      },
    },
  },
  plugins: [],
}
