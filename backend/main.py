from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api import router as api_router
import os

app = FastAPI(title="AI Vision Enhancement & Detection Lab", 
              description="Demonstrates image enhancement algorithms and their impact on YOLOv5 object detection.",
              version="1.0.0")

# Configure CORS for deployment
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # In production, you might want to restrict this to your frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Foggy Image Enhancer API is running. Use /api/process for image processing."}

app.include_router(api_router, prefix="/api")

# Create a temporary directory for processing if it doesn't exist
os.makedirs("temp", exist_ok=True)

if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
