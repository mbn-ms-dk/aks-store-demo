from fastapi import FastAPI, status
from routers.description_generator import description
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import   JSONResponse
import json

app = FastAPI()
app.include_router(description)
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])


@app.get("/health", summary="check if server is healthy", operation_id="health")
async def get_products():
    """
    Returns status code 200
    """
    return JSONResponse(content={"status": 'ok'}, status_code=status.HTTP_200_OK)
