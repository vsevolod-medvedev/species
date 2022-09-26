from app import config
from app.server import Server

if __name__ == '__main__':
    Server().run(host=config.APP_HOST, port=config.APP_PORT)
