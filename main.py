from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import uvicorn
from typing import Optional

app = FastAPI(title="Chat Streaming API", version="1.0.0")

class ChatRequest(BaseModel):
    message: str
    system_prompt: Optional[str] = None

class ChatResponse(BaseModel):
    response: str
    status: str

@app.get("/")
async def root():
    return {"message": "Chat Streaming API is running"}

@app.post("/chat-news-stream", response_model=ChatResponse)
async def chat_endpoint(request: ChatRequest):
    """
    Streams 'thinking' and 'main' responses for a news query.
    - Gets news from Apache Solr.
        # right now using static prompt
    - Uses a smaller model to generate 'thinking' output.
    - Uses a larger model for the main result.
    - Streams 'thinking' until the first chunk of the main result arrives, then streams the main result.
    """
    try:
        # For now, return a static response
        # TODO: Implement actual chat logic with streaming
        static_response = f"You said: {request.message}. This is a static response for testing."
        
        return ChatResponse(
            response=static_response,
            status="success"
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)