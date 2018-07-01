import api
from flask import Flask

from app.api import rule, event, user
from app.db import engine, Base

app = Flask(__name__)


# Create Blueprints
app.register_blueprint(rule)
app.register_blueprint(event)
app.register_blueprint(user)

# Create tables
Base.metadata.create_all(engine)
