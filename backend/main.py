import os
import httpx
import base64
from fastapi import FastAPI, UploadFile, HTTPException, Form
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(title="Audio Transcription API")

# Configuration CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["POST"],
    allow_headers=["*"],
)

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
if not OPENROUTER_API_KEY:
    raise ValueError("OPENROUTER_API_KEY non définie dans .env")

@app.post("/process-audio")
async def process_audio(
    audio: UploadFile,
    prompt: str = Form("Vous êtes un assistant utile. Écoutez attentivement cette audio et comprenez ce que l'utilisateur demande. Répondez ensuite de manière appropriée et utile à la demande formulée dans l'audio. Ne vous contentez pas de répéter ce qui est dit, mais fournissez une vraie réponse à la question ou à la demande."),
    model: str = Form("google/gemini-2.5-flash"),
    web_search_enabled: str = Form("false")
):
    """Traite un fichier audio avec un LLM via OpenRouter."""

    if not audio.content_type.startswith("audio/"):
        raise HTTPException(400, "Le fichier doit être un audio")

    # Configuration de la recherche web
    web_search_enabled_bool = web_search_enabled.lower() == "true"
    final_model = model
    plugins = None

    if web_search_enabled_bool:
        # Pour les modèles OpenAI, utiliser le suffixe :online
        if model.startswith("openai/"):
            final_model = f"{model}:online"
        else:
            # Pour les autres modèles, utiliser le plugin web
            plugins = [{"id": "web"}]

    try:
        # Lecture du fichier audio
        audio_content = await audio.read()

        # Encodage en base64
        base64_audio = base64.b64encode(audio_content).decode('utf-8')

        # Détermination du format audio
        content_type = audio.content_type
        if content_type == "audio/wav" or audio.filename.endswith('.wav'):
            audio_format = "wav"
        elif content_type == "audio/mpeg" or content_type == "audio/mp3" or audio.filename.endswith('.mp3'):
            audio_format = "mp3"
        else:
            # Format par défaut si non reconnu
            audio_format = "wav"

        # Appel à OpenRouter Chat Completions API avec input_audio
        request_data = {
            "model": final_model,
            "messages": [
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": prompt
                        },
                        {
                            "type": "input_audio",
                            "input_audio": {
                                "data": base64_audio,
                                "format": audio_format
                            }
                        }
                    ]
                }
            ]
        }

        # Ajouter les plugins si nécessaire
        if plugins:
            request_data["plugins"] = plugins

        async with httpx.AsyncClient() as client:
            response = await client.post(
                "https://openrouter.ai/api/v1/chat/completions",
                headers={
                    "Authorization": f"Bearer {OPENROUTER_API_KEY}",
                    "Content-Type": "application/json"
                },
                json=request_data
            )

            if response.status_code != 200:
                raise HTTPException(500, f"Erreur API: {response.text}")

            result = response.json()

            # Extraction de la réponse du LLM
            if "choices" in result and len(result["choices"]) > 0:
                response_text = result["choices"][0]["message"]["content"]
                return JSONResponse({
                    "response": response_text,
                    "model": result.get("model", final_model),
                    "usage": result.get("usage", {}),
                    "web_search_enabled": web_search_enabled_bool
                })
            else:
                raise HTTPException(500, "Réponse API invalide")

    except Exception as e:
        raise HTTPException(500, f"Erreur transcription: {str(e)}")

@app.get("/health")
async def health():
    """Endpoint de santé."""
    return {"status": "ok"}
