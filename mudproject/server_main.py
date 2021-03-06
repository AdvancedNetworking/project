from flask import Flask

import time, traceback
from handlers.routes import configure_routes

app = Flask(__name__)

configure_routes(app)

if __name__ == '__main__':
    app.run()
