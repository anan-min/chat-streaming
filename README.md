# Chat Streaming with Ollama & FastAPI

This project streams chat responses from Ollama models using Python.  
It demonstrates how to run a "thinking" prompt on a smaller model and a main prompt on a larger model, streaming both outputs to the console.

## Features

- Streams model output in real time
- Runs two prompts in parallel (thinking + main)
- Stops the "thinking" stream when the main model starts responding

## Why Use a Smaller Model for Thinking?

Most large language models generate "thinking" steps in English or the language they were primarily trained on.  
To avoid the need for expensive fine-tuning, this project uses a smaller model to simulate the "thinking" process.  
This is a practical workaround: the smaller model can replicate step-by-step reasoning, allowing the main model to focus on generating the final answer in your target language.

## Requirements

- Python 3.11+
- [Ollama](https://ollama.com/) running locally with required models pulled
- Docker (optional, for containerization)

## Setup

1. **Clone the repository:**
   ```sh
   git clone <your-repo-url>
   cd chat-streaming
   ```

2. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

3. **Ensure Ollama is running and models are available:**
   ```sh
   ollama pull qwen2.5:1.5b
   ollama pull qwen2.5:7b
   ```

4. **Run the script:**
   ```sh
   python main.py
   ```

## Docker Usage

1. **Build the Docker image:**
   ```sh
   docker build -t chat-streaming .
   ```

2. **Run the container:**
   ```sh
   docker run --rm -it chat-streaming
   ```

> **Note:** Ollama must be accessible from inside the container.  
> For local development, run Ollama on your host and set up networking if needed.

## Customization

- Edit `prompt.py` to change the prompts.
- Change model names in `main.py` as needed.

---

Let me know if you need FastAPI endpoints or further Docker networking instructions!