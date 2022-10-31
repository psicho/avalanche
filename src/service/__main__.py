import uvicorn
from service.server import app
from service.settings import config

if __name__ == "__main__":
    uvicorn.run(app, host=config.HOST, port=config.PORT)
