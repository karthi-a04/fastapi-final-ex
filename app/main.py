import os
import logging
import logging_loki
from fastapi import FastAPI

SERVICE_NAME = os.getenv("SERVICE_NAME", "unknown_service")

handler = logging_loki.LokiHandler(
    url="http://loki-gateway.loki.svc.cluster.local/",
    tags={"service": SERVICE_NAME},   # ← this becomes the label in Grafana
    version="1",
)

logger = logging.getLogger("app")
logger.setLevel(logging.INFO)
logger.addHandler(handler)

app = FastAPI()

@app.get("/")
def read_root():
    logger.info("Root endpoint hit")
    return {"message": f"Hello from {SERVICE_NAME}"}

@app.get("/health")
def health():
    logger.info("Health check")
    return {"status": "ok", "service": SERVICE_NAME}