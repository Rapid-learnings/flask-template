from flask import Blueprint, jsonify
from app.services.Login import token_required
from app.common.database import User

user_blueprint = Blueprint('user', __name__)
@user_blueprint.route('/user', methods=['GET'])
@token_required
def get_all_users(current_user):
#def get_all_users():
	users = User.query.all()

	output = []
	for user in users:

		output.append({
			'id' : user.id,
			'public_id': user.public_id,
			'name' : user.name,
			'email' : user.email,
			'created_at' : user.created_at
		})

	return jsonify({'users': output})
