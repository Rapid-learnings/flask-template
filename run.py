import logging
import os

from dotenv import load_dotenv
from flask import Flask

from app.v1.project import project

from extensions import make_celery, db

from app.services.Signup import signup_blueprint
from app.services.Login import login_blueprint
from app.services.GetUser import user_blueprint

app = Flask(__name__)

load_dotenv()

# Logger
logging.basicConfig(level=logging.DEBUG,
                    format='[%(asctime)s]: {} %(levelname)s %(message)s'.format(
                        os.getpid()),
                    datefmt='%Y-%m-%d %H:%M:%S',
                    handlers=[logging.StreamHandler()])
LOGGER = logging.getLogger()

app.config.update(
    FLASK_ENV=os.getenv('FLASK_ENV'),
    DEBUG=os.getenv('DEBUG'),
    CELERY_RESULT_BACKEND=os.getenv('CELERY_RESULT_BACKEND'),
    CELERY_BROKER_URL=os.getenv('CELERY_BROKER_URL')
)

# Setup MySQL Settings
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')
app.config['SQLALCHEMY_ECHO'] = bool(os.getenv('SQLALCHEMY_ECHO'))
app.config['SQLALCHEMY_RECORD_QUERIES'] = bool(
    os.getenv('SQLALCHEMY_RECORD_QUERIES'))
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = os.getenv(
    'SQLALCHEMY_TRACK_MODIFICATIONS')


db.init_app(app)


def _dispose_db_pool():
    with app.app_context():
        db.engine.dispose()


# try:
#     from uwsgidecorators import postfork
#
#     postfork(_dispose_db_pool)
# except ImportError:
#     # Implement fallback when running outside of uwsgi...
#     raise
#

@app.route('/')
def hello_world():
    return 'Hello World!!'


# Register blueprints
app.register_blueprint(project)

app.register_blueprint(signup_blueprint)
app.register_blueprint(login_blueprint)
app.register_blueprint(user_blueprint)

celery = make_celery(app)


if __name__ == '__main__':
    app.run(debug=True)
