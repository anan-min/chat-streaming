# Chat Streaming API with FastAPI & Ollama

A FastAPI-based chat streaming application that integrates with Ollama for AI-powered conversations.

## Features

- **FastAPI REST API** with automatic OpenAPI documentation
- **Static chat endpoint** (ready for streaming enhancement)
- **Ollama integration** for AI model interactions
- **Docker support** with production-ready configuration
- **Health check endpoints** for monitoring

## API Endpoints

- `GET /` - Root endpoint with API status
- `POST /chat` - Chat endpoint accepting messages and optional system prompts
- `GET /health` - Health check endpoint
- `GET /docs` - Interactive API documentation (Swagger UI)
- `GET /redoc` - Alternative API documentation

## Requirements

- Python 3.11+
- [Ollama](https://ollama.com/) running locally with required models
- Docker (optional, for containerization)

## Local Development

1. **Clone the repository:**
   ```bash
   git clone <your-repo-url>
   cd chat-streaming
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Ensure Ollama is running with required models:**
   ```bash
   ollama pull qwen2.5:1.5b
   ollama pull qwen2.5:7b
   ```

4. **Run the FastAPI server:**
   ```bash
   python main.py
   ```
   
   Or with uvicorn directly:
   ```bash
   uvicorn main:app --host 0.0.0.0 --port 8000 --reload
   ```

5. **Access the API:**
   - API: http://localhost:8000
   - Documentation: http://localhost:8000/docs
   - Alternative docs: http://localhost:8000/redoc

## Docker Usage

### Build and Run

```bash
# Build the image
docker build -t chat-streaming-api .

# Run the container
docker run -p 8000:8000 --name chat-api chat-streaming-api
```

### Docker Compose (with Ollama)

Create a `docker-compose.yml`:

```yaml
version: '3.8'
services:
  chat-api:
    build: .
    ports:
      - "8000:8000"
    depends_on:
      - ollama
    environment:
      - OLLAMA_BASE_URL=http://ollama:11434

  ollama:
    image: ollama/ollama
    ports:
      - "11434:11434"
    volumes:
      - ollama_data:/root/.ollama

volumes:
  ollama_data:
```

## API Usage Examples

### Chat Request

```bash
curl -X POST "http://localhost:8000/chat" \
     -H "Content-Type: application/json" \
     -d '{
       "message": "Hello, how are you?",
       "system_prompt": "You are a helpful assistant."
     }'
```

### Response Format

```json
{
  "response": "You said: Hello, how are you?. This is a static response for testing.",
  "status": "success"
}
```

## Project Structure

```
chat-streaming/
├── main.py              # FastAPI application
├── streaming.py         # Streaming logic (to be integrated)
├── prompt.py           # Prompt definitions
├── requirements.txt    # Python dependencies
├── Dockerfile         # Container configuration
├── .gitignore        # Git ignore rules
└── README.md         # This file
```

## Development Roadmap

- [ ] Implement streaming responses using Server-Sent Events (SSE)
- [ ] Integrate existing streaming.py functionality
- [ ] Add authentication and rate limiting
- [ ] Add conversation history management
- [ ] Implement WebSocket support for real-time chat

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

---

**Note:** This is currently a base template with static responses. Streaming functionality will be implemented in the next iteration.