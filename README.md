# Audio2LLM 🎤🤖

A model-agnostic audio processing application inspired by ChatGPT's transcribe feature. This weekend project lets you record audio and have it processed by various LLMs via OpenRouter.

## What it does

Record audio → Process with any LLM → Get intelligent responses (not just transcription, but actual AI analysis and responses)

## Structure du projet

```
audio2llm/
├── backend/
│   ├── main.py           # FastAPI server
│   ├── requirements.txt  # Python dependencies
│   └── .env (à créer)   # Environment variables
├── frontend/
│   ├── src/             # Svelte TypeScript source
│   ├── package.json     # Node.js dependencies
│   └── vite.config.ts   # Vite configuration
└── README.md
```

## Technologies utilisées

- **Backend**: FastAPI (Python) with async support
- **Frontend**: Svelte + TypeScript + Vite
- **Audio Processing**: Browser MediaRecorder API
- **AI Models**: OpenRouter API (supporting multiple LLM providers)

## Setup & Running

### 1. Configuration

Create `backend/.env` with your OpenRouter API key:
```env
OPENROUTER_API_KEY=your_api_key_here
```

**That's the only environment variable you need!** 🎉

### 2. Backend Setup

```bash
cd backend
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload --port 8000
```

### 3. Frontend Setup

```bash
cd frontend
npm install
npm run dev
```

Open http://localhost:5173 in your browser.

## Features

- 🎙️ **Record audio** directly in the browser
- 🤖 **Model flexibility** - Choose from various LLMs (Google Gemini, OpenAI GPT, etc.)
- 🧠 **Smart responses** - Not just transcription, but intelligent analysis of your audio
- 🔍 **Web search** - Enable web search for some models to get up-to-date information
- ✨ **Modern UI** - Clean Svelte interface with real-time feedback
- 🔄 **Error handling** - Robust error management throughout

## Available Models

The app includes various models from different providers:
- Google Gemini (2.0 Flash, 2.5 Flash, 2.5 Pro variants)
- OpenAI GPT-4o (including audio preview)
- And more...

⚠️ **Note**: Model IDs are hardcoded and may change as providers update their offerings.

## About This Project

This is a **small personal weekend project** - a "vibe-coded" implementation inspired by ChatGPT's transcribe feature, but made model-agnostic to work with various LLM providers through OpenRouter.

### Architecture Highlights

- **FastAPI backend** - Modern Python with async support and automatic API docs
- **Svelte frontend** - Reactive UI with TypeScript for type safety
- **Single endpoint** - Clean `/process-audio` API that handles everything
- **OpenRouter integration** - Access to multiple LLM providers with one API
- **Browser-native audio** - Uses MediaRecorder API, no external dependencies

The goal was to create something similar to ChatGPT's audio feature but with the flexibility to use different models and providers.
