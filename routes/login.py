from flask import Blueprint, request
from models.users import Users, UsersSchema
from utils.configdb import db
from werkzeug.security import check_password_hash
from flask_jwt_extended import create_access_token
from datetime import timedelta

LoginRoute = Blueprint('login', __name__)
userSchema = UsersSchema()

@LoginRoute.route('/login')
def login():
    try:
        user_email = request.json['user_email']
        user_password = request.json['user_password']
        user = Users.query.filter_by(user_email = user_email).first()
        if user:
            passwordHashed = user.user_password
            validatePassword = check_password_hash(passwordHashed, user_password)
            if validatePassword:
                access_token = create_access_token(identity=user.user_fullname, expires_delta= timedelta(hours=1))
                return {'access_token': access_token}, 200
            return {'access_token': validatePassword}, 200

        return {'access_token': False}, 200
    
    except Exception as e:
        print(e)
        return {'error': 'Error trying login'}, 500