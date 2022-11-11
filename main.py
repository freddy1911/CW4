from flask import Flask
from flask_restx import Api

from config import Config
from setup_db import db
from views.auth import auth_ns
from views.director import director_ns
from views.genre import genre_ns
from views.movie import movie_ns
from views.user import user_ns


def create_app(config: Config) -> Flask:
    application = Flask(__name__)
    application.config.from_object(config)
    application.app_context().push()
    return application


def configure_app(application: Flask):
    db.init_app(application)
    api = Api(app)
    api.add_namespace(director_ns)
    api.add_namespace(movie_ns)
    api.add_namespace(genre_ns)
    api.add_namespace(auth_ns)
    api.add_namespace(user_ns)


app = create_app(Config())
app.debug = True
app_config = Config()
app = create_app(app_config)
configure_app(app)
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run()
