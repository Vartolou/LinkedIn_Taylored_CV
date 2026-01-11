#!/bin/bash

# Start Backend
echo "🚀 Starting Li-Taylored CV Backend..."
cd backend
python main.py &

# Wait for backend to start
sleep 3

# Start Frontend
echo "🚀 Starting Li-Taylored CV Frontend..."
cd ..
npm run dev
