from flask import Blueprint, Flask, request, jsonify, make_response
from app.common.database import User
from werkzeug.security import generate_password_hash
import uuid
from extensions import db

signup_blueprint = Blueprint('signup', __name__)
@signup_blueprint.route('/signup', methods=['POST'])
def signup():
	data = request.form
	# gets name, email and password
	name, email = data.get('name'), data.get('email')
	password = data.get('password')
	# checking for existing user
	# user = User.query\
	# 	.filter_by(email = email)\
	# 	.first()
	user = User.query.filter_by(email = email).first()
	if not user:
		# database ORM object
		user = User(
			public_id = str(uuid.uuid4()),
			name = name,
			email = email,
			password = generate_password_hash(password)
		)
		# insert user
		db.session.add(user)
		db.session.commit()

		return make_response('Successfully registered.', 201)
	else:
		return make_response('User already exists. Please Log in.', 202)
