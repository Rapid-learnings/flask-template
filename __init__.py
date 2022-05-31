from flask import Blueprint
project = Blueprint('project', __name__, url_prefix='/api/v1')
from.import controller
