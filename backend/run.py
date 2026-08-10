from translate.config import Config
from translate.app import create_app

app = create_app(Config())

if __name__ == '__main__':
    app.run()
