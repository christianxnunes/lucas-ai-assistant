# 🤖 Lucas AI Assistant 
Assistente de voz inteligente rodando localmente com IA, reconhecimento de fala e resposta por voz.
---

## 🚀 Sobre o projeto

O Lucas AI Assistant é um assistente virtual orientado a voz, projetado para oferecer interação natural em tempo real por meio de inteligência artificial executando localmente. Inspirado em soluções como Alexa e Jarvis, o projeto foi desenvolvido com foco em arquitetura simples, eficiente e escalável, explorando conceitos modernos de integração entre frontend e backend.

A solução combina reconhecimento de fala no navegador com um backend em Python utilizando FastAPI, responsável por orquestrar a comunicação com modelos de linguagem locais via Ollama. Esse fluxo permite capturar comandos de voz, processar linguagem natural e retornar respostas de forma fluida, com baixa latência e sem dependência de serviços externos.

Além da interação por voz, o projeto implementa geração de resposta falada diretamente pelo sistema operacional, garantindo compatibilidade com cenários como streaming e automação. A escolha por IA local reforça aspectos importantes como privacidade, controle de dados e redução de custos operacionais.

Do ponto de vista técnico, o projeto aborda:

- Integração entre frontend web e backend assíncrono
- Consumo de modelos de linguagem local (LLM)
- Processamento de linguagem natural em tempo real
- Controle de estado para interação contínua por voz
- Orquestração de serviços e automação de inicialização (Ollama + API)

O Lucas AI Assistant demonstra a aplicação prática de conceitos modernos de desenvolvimento, sendo uma base sólida para evolução em áreas como assistentes inteligentes, automação por voz e produtos baseados em IA.

---

## 🎯 Objetivo

Criar um assistente de voz que seja:

- 🎤 Capaz de ouvir comandos por voz continuamente
- 🧠 Inteligente com respostas naturais usando IA local
- 🔊 Capaz de responder com voz automaticamente
- 🖥️ Capaz de monitorar a tela e tomar decisões baseadas em informações da tela
- 🤖 Capaz de manipular objetos reais em tempo real
- ⚡ Hands-free (sem necessidade de clicar)
- 💻 100% local e gratuito
- ⚡ Capaz de clonar o projeto e ao rodar o comando `pip install -r requirements.txt` ele instale as dependências do projeto e o modelo de IA local.
- ⚡ Capaz de não precisar de um arquivo `index.html` para rodar o projeto, apenas rodar o comando `python main.py` e o projeto rodará na porta 3000.

---

## 🧠 Tecnologias utilizadas

- Python (FastAPI)
- JavaScript (SpeechRecognition API)
- Ollama (IA local)
- pyttsx3 (Text-to-Speech)
- HTML + JS

---

## 🧠 Instalando o Ollama

Baixe em:
```bash
https://ollama.com/
```

Depois execute:

```bash
ollama pull gemma4:e2b
```
---

## 📦 Instalação
Clone o repositório:

```bash
git clone https://github.com/SEU-USUARIO/lucas-ai-assistant.git
cd lucas-ai-assistant
```

Instale as dependências:
```bash
pip install fastapi uvicorn requests pyttsx3
```
---

## ▶️ Como rodar
```bash
python main.py
```
Acesse:
```bash
http://localhost:3000
```
---

## 🎤 Como usar
1. Abra o projeto no navegador
2. Permita acesso ao microfone
3. Fale:
   👉 "Lucas"
4. Depois faça sua pergunta.

🛑 **Comandos disponíveis**
- `"Lucas"` → ativa o assistente
- `"Lucas espera"` → pausa

🧠 **Como funciona**
1. O navegador captura sua voz
2. Converte para texto
3. Envia para o backend (FastAPI)
4. O backend consulta a IA local (Ollama)
5. Retorna a resposta
6. O Python reproduz a fala

🔊 **Observação importante**
A voz é gerada pelo Python (`pyttsx3`), e não pelo navegador.

Isso permite integração com softwares de streaming como:
- OBS
- TikTok Live Studio
