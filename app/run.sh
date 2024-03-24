#!/bin/bash

# Start the backend
echo "Starting backend server..."
cd Backend
uvicorn main:app --reload --port 3000 &

# Get back to the root directory
cd ..

# Start the frontend
echo "Starting frontend..."
cd Frontend
npm install
npm run dev 
