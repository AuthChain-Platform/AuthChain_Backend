from config import Config
from fastapi import FastAPI
from app.routes import setup_routes

app = FastAPI(
    title="QR Code Scanner API",
    description="An API for QR Code scanning using authChain",
    version="1.0.0"
)

setup_routes(app)

@app.get("/")
def root():
    return {"message": "Welcome to the QR Scanner API"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("server:app", host=Config.HOST, port=Config.PORT, reload=Config.DEBUG)
