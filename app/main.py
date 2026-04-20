import os
import logging
from fastapi import FastAPI

logging.basicConfig(level=logging.INFO)

app = FastAPI()

SERVICE_NAME = os.getenv("SERVICE_NAME", "unknown")

@app.get("/")
def read_root():
    logging.info(f"Request hit {SERVICE_NAME}")
    return {"message": f"Hello from {SERVICE_NAME}"}