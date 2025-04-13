import os
import logging
from datetime import datetime

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from werkzeug.middleware.proxy_fix import ProxyFix
from flask_login import LoginManager


# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)

# Create the app
app = Flask(__name__)
app.secret_key = os.environ.get("SESSION_SECRET", "desarrollo_secreto_cosmico")
app.wsgi_app = ProxyFix(app.wsgi_app, x_proto=1, x_host=1)  # needed for url_for to generate with https

# Configure the database
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL", "postgresql://postgres:postgres@localhost/cosmos")
app.config["SQLALCHEMY_ENGINE_OPTIONS"] = {
    "pool_recycle": 300,
    "pool_pre_ping": True,
}
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Initialize Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'
login_manager.login_message = 'Por favor inicia sesión para acceder a esta página.'

# Initialize the app with the extension
db.init_app(app)

# Context processor to provide date/time to all templates
@app.context_processor
def inject_now():
    return {'now': datetime.now()}

with app.app_context():
    # Import models and routes
    import models
    from routes import init_routes
    
    # Initialize routes
    init_routes(app)
    
    # Create database tables
    db.create_all()

    # Load user loader function from models
    from models import User
    
    @login_manager.user_loader
    def load_user(user_id):
        return db.session.get(User, int(user_id))
