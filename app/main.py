import os
import logging
from fastapi import FastAPI
from pythonjsonlogger import jsonlogger

# Set up JSON logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)
handler = logging.StreamHandler()
formatter = jsonlogger.JsonFormatter()
handler.setFormatter(formatter)
logger.addHandler(handler)

app = FastAPI()

SERVICE_NAME = os.getenv("SERVICE_NAME", "unknown_service")

@app.get("/")
def read_root():
    logging.info("Request hit", extra={"service": SERVICE_NAME})
    return {"message": f"Hello from {SERVICE_NAME}"}