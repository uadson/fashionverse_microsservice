from fastapi import FastAPI
from ze import config

app = FastAPI(title="Products Service - FashionVerse")

@app.get("/")
async def root():
    db_url_status = "loaded" if config('DATABASE_URL') else "don't loaded"
    return {"message": f"Products service on live! DB URL: {db_url_status}"}