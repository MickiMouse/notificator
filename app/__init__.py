import os

from flask import Flask, jsonify
from flask_pymongo import PyMongo

from werkzeug.exceptions import HTTPException


mongo = PyMongo()


def create_app(environment='development'):

    from config import config

    app = Flask(__name__)

    env = os.environ.get('FLASK_ENV', environment)
    app.config.from_object(config[env])
    config[env].configure(app)

    mongo.init_app(app)

    with app.app_context():
        from .main import main_blueprint
        app.register_blueprint(main_blueprint)

    @app.errorhandler(HTTPException)
    def handle_http_error(exc):
        return jsonify({
            'error': {
                'description': exc.description,
                'status_code': exc.code
            }
        })

    return app
