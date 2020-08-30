from flask import Flask

app = Flask(__name__)

import main.views
from main.config import configure_app

app = Flask(__name__, instance_relative_config=True)
configure_app(app)