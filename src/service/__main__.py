import uvicorn
from src.service.server import app
from src.service.settings import config

if __name__ == "__main__":
    uvicorn.run(app, host=config.HOST, port=config.PORT)
