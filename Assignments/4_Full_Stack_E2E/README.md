# Multimodal Personal Expense Assistant

Full-stack AI expense tracker with Google ADK, Gemini 2.0, RAG, and Firebase.

## 🎯 Overview
Demonstrates a complete multimodal AI agent with receipt OCR, natural language queries, RAG-powered search, and real-time analytics.

## 🛠️ Tech Stack
- **Frontend**: React + TypeScript + Material-UI
- **Backend**: FastAPI + Google ADK + Gemini 2.0 Flash
- **Database**: Firebase Firestore + Vertex AI Vector Search
- **Features**: Receipt OCR, NLP queries, RAG, expense analytics

## 🚀 Quick Start

### Backend
```bash
cd backend
pip install -r requirements.txt
cp .env.example .env  # Add your GCP credentials
uvicorn app.main:app --reload
```

### Frontend
```bash
cd frontend
npm install
cp .env.example .env  # Add API URL
npm start
```

**Access**: Frontend at `localhost:3000` | API at `localhost:8000`

## 📁 Project Structure
```
├── frontend/          # React app
│   └── src/          # Components, services, types
├── backend/           # FastAPI + ADK agent
│   └── app/          # main.py, agent.py, database.py
├── database/          # Firebase setup
└── docs/              # Documentation
```

## ✨ Key Features
- 📸 Upload receipts → AI extracts expense data
- 💬 Natural language queries about spending
- 🔍 RAG-powered semantic search
- 📊 Real-time expense analytics
- 🤖 Multi-turn conversations with context

## 📖 API Docs
Swagger: `http://localhost:8000/docs`

## 🎥 Video Walkthrough
[Code Walkthrough & Demo](https://youtube.com/placeholder-link-e)

## 🔗 References
- [Google Codelab](https://codelabs.developers.google.com/personal-expense-assistant-multimodal-adk)
- [Medium Article](https://medium.com/google-cloud/going-multimodal-with-agent-development-kit-personal-expense-assistant-with-gemini-2-5-480b031c7d5a)

## 📝 License
MIT License