from fastapi import FastAPI
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

# Log a message when the application starts
logger.info("FastAPI application has started.")

@app.get("/")
async def read_root():
    # Log a message when the root endpoint is accessed
    logger.info("Root endpoint was accessed.")
    return {"message": "Hello, World from app!"} 