import os
from flask import Flask
from dotenv import load_dotenv
from neuroflow.routes import user, mood
from neuroflow.extensions import db
import os
from flask_cors import CORS 

def create_app():
    load_dotenv()

    app = Flask(__name__, static_folder='static')
    app.config['ENV'] = os.getenv('FLASK_ENV')
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DB')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
    app.config['PORT'] = os.getenv('FLASK_PORT')
    cors = CORS(app, resources={r"/*": {"origins": os.getenv('FRONTEND_URL')}})
    app.config['CORS_HEADERS'] = 'Content-Type'
    register_extensions(app)
    register_blueprints(app)
    if app.config['ENV'] == 'development':
        with app.app_context():
            db.drop_all()
            db.create_all()

    return app
    
def register_extensions(app):
    db.init_app(app)

def register_blueprints(app):
    app.register_blueprint(user.blueprint)
    app.register_blueprint(mood.blueprint)


