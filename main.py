import subprocess
import time
import requests
import os
import threading
import pyttsx3

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse, FileResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# 🔊 inicializar voz
engine = pyttsx3.init()

def falar(texto):
    def run():
        engine.say(texto)
        engine.runAndWait()
    threading.Thread(target=run).start()

# 🌐 CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 🚀 iniciar Ollama
def iniciar_ollama():
    try:
        requests.get("http://localhost:11434")
        print("🟢 Ollama já está rodando")
    except:
        print("🚀 Iniciando Ollama...")
        subprocess.Popen(
            ["ollama", "serve"],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )
        time.sleep(3)

# 📥 garantir modelo
def carregar_modelo():
    print("📥 Verificando modelo gemma4:e2b...")
    subprocess.run(["ollama", "pull", "gemma4:e2b"])

# 🧠 CHAT
@app.post("/chat")
async def chat(data: dict):
    message = data.get("message")

    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "gemma4:e2b",
                "prompt": f"""
                    Você é Lucas, um assistente de voz inteligente.

                    Fale como um humano em uma conversa por voz.
                    Seja natural, direto e fluido.
                    Não use emojis.
                    Não use asteriscos, markdown ou formatação.
                    Não enumere respostas.
                    Não escreva como texto de chat.
                    Evite frases robóticas ou formais demais.

                    Responda como alguém conversando normalmente.

                    Pergunta:
                    {message}

                    Resposta:
                    """,
                "stream": False
            }
        )

        data = response.json()
        resposta = data.get("response")

        # 🔊 falar pelo Python
        falar(resposta)

        return {"reply": resposta}

    except Exception as error:
        print(error)
        return JSONResponse(
            content={"reply": "Erro ao responder"},
            status_code=500
        )

# 🌐 home
@app.get("/")
def home():
    return FileResponse("public/index.html")

# 📁 static
app.mount("/static", StaticFiles(directory="public"), name="static")

# ▶️ start
if __name__ == "__main__":
    if not os.path.exists("public"):
        os.makedirs("public")

    iniciar_ollama()
    carregar_modelo()

    import uvicorn
    print("🚀 Lucas rodando em http://localhost:3000")
    uvicorn.run(app, host="0.0.0.0", port=3000)