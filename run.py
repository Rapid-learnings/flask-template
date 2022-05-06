import logging
import os

from dotenv import load_dotenv
from flask import Flask


from app.commands.example import register_commands
from app.v1.project import project

from extensions import make_celery, db
#from app.lib.kafka_package import Consumer
import Consumer

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
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')
app.config['SQLALCHEMY_ECHO'] = bool(os.getenv('SQLALCHEMY_ECHO'))
app.config['SQLALCHEMY_RECORD_QUERIES'] = bool(
    os.getenv('SQLALCHEMY_RECORD_QUERIES'))
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = os.getenv(
    'SQLALCHEMY_TRACK_MODIFICATIONS')
#setup Kafka
# app.config['KAFKA_HOSTNAME'] = os.getenv(
#     'KAFKA_HOSTNAME')

db.init_app(app)


print("--------start----------")
@app.route('/')
def hello_world():
   
    return Consumer.got_fun()
    return 'Hello Rapid!!'

print("--------End----------")




# Register blueprints
app.register_blueprint(project)

celery = make_celery(app)

register_commands(app)
#-----kafka-------#
#producer=make_producer(app)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5005 ,debug=True)
