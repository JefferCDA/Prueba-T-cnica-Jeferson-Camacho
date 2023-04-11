from flask import Blueprint, request
from models.users import Users, UsersSchema
from utils.configdb import db
from werkzeug.security import check_password_hash


usersRoutes = Blueprint('users', __name__)

manyUsersSchema = UsersSchema(many= True)
userSchema = UsersSchema()

@usersRoutes.route('/users', methods = ['POST'])
def setUsers():
    try:
        user_fullname = request.json['user_fullname']
        user_email = request.json['user_email']
        user_password = request.json['user_password']
        user_address = request.json['user_address']
        user_phone = request.json['user_phone']
        user_date = request.json['user_date']

        
        newUser = Users(user_fullname, user_email, user_password, user_address, user_phone, user_date)
        db.session.add(newUser)
        db.session.commit()


        return userSchema.jsonify(newUser)
    
    except Exception as e:
        print(e)
        return {'error': 'Error trying to set user'}, 500



@usersRoutes.route('/users', methods = ['GET'])
def getUsers():
    try:
        allUsers = Users.query.all()
        return manyUsersSchema.jsonify(allUsers)
    
    except Exception as e:
        print(e)
        return {'error': 'Error trying to get news'}, 500

@usersRoutes.route('/users/<id>', methods = ['GET'])
def getUser(id):
    try:
        user = Users.query.filter_by(id = id).first()
        if user is None:
            return {'error':'This user does not exist'}, 404
        return userSchema.jsonify(user)
    
    except Exception as e:
        print(e)
        return {'error': 'Error trying to get user'}, 500

@usersRoutes.route('/users/<id>', methods = ['PUT'])
def updateUser(id):
    try:
        user = Users.query.filter_by(id = id).first()
        if user is None:
            return {'error':'This user does not exist'}, 404
        
        user_fullname = request.json['user_fullname']
        user_email = request.json['user_email']
        user_password = request.json['user_password']
        user_address = request.json['user_address']
        user_phone = request.json['user_phone']
        user_date = request.json['user_date']

        passwordHashed = user.user_password
        validatePassword = check_password_hash(passwordHashed, user_password)

        if validatePassword:
            user.user_fullname = user_fullname
            user.user_email = user_email
            user.user_password = user_password
            user.user_address = user_address
            user.user_phone = user_phone
            user.user_date = user_date

            db.session.commit()
            return userSchema.jsonify(user)
        return  {'error': 'incorrect password'}, 500
    except Exception as e:
        print(e)
        return {'error': 'Error trying to update user'}, 500
    