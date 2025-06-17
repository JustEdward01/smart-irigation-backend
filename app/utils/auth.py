from fastapi import Header, HTTPException
import os

API_SECRET = os.getenv("API_SECRET", "fallback_secret")
print(f"API_SECRET backend: {API_SECRET}")

def verify_api_key(x_api_key: str = Header(...)):
    if x_api_key != API_SECRET:
        raise HTTPException(status_code=403, detail="Invalid API key")
