# Audio → Texte - Application de transcription audio

Application élégante et minimaliste pour l'enregistrement audio et la transcription via OpenRouter.

## Structure du projet

```
audio-transcription/
├── backend/
│   ├── main.py
│   ├── requirements.txt
│   └── .env (à créer)
├── frontend/
│   └── index.html
└── README.md
```

## Technologies utilisées

- **Backend**: FastAPI (Python) - Framework moderne avec support async natif
- **Frontend**: HTML5 vanilla - Interface native avec MediaRecorder API
- **Transcription**: OpenRouter Whisper API

## Instructions de lancement

### 1. Installation du backend

```bash
cd backend
python -m venv venv
source venv/bin/activate  # Sur Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 2. Configuration

Créer le fichier `backend/.env` avec votre clé API OpenRouter :
```env
OPENROUTER_API_KEY=votre_clé_api
```

### 3. Démarrage

**Backend :**
```bash
cd backend
uvicorn main:app --reload --port 8000
```

**Frontend :**
```bash
cd frontend
python -m http.server 3000
```

Ouvrir http://localhost:3000 dans le navigateur.

## Fonctionnalités

- 🎙️ Enregistrement audio en temps réel via le navigateur
- 📝 Transcription automatique via OpenRouter Whisper
- ✨ Interface utilisateur élégante et intuitive
- ⚡ Feedback visuel immédiat pendant l'enregistrement
- 🔄 Gestion d'erreurs complète

## Points clés de l'implémentation

### ✨ Élégance et simplicité

- **Pas de dépendances inutiles** : HTML5 vanilla côté front, FastAPI minimal côté back
- **Code concis** : ~200 lignes au total pour une application complète
- **Interface épurée** : UX intuitive avec feedback visuel immédiat
- **Architecture claire** : Séparation nette front/back, un seul endpoint

### 🎯 Choix techniques justifiés

- **FastAPI** : Framework Python moderne, async natif, documentation automatique
- **HTML5 MediaRecorder API** : Solution native du navigateur, pas besoin de librairies
- **CORS minimal** : Configuration simple pour le développement local
- **Pas de bundler** : Un seul fichier HTML self-contained

Cette implémentation privilégie la simplicité sans sacrifier la fonctionnalité ni l'expérience utilisateur.
