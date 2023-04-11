from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_jwt_extended import JWTManager
from utils.configdb import db

# All declarations routes 
from routes.users import usersRoutes
from routes.news import newsRoutes
from routes.comments import CommentsRoutes
from routes.login import LoginRoute


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://root:meinsm@localhost/backendtestdb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
app.config['JWT_SECRET_KEY'] = 'testbackSecretKeyJWT'

SQLAlchemy(app)
Marshmallow(app)
JWTManager(app)

with app.app_context():
    db.create_all()

app.register_blueprint(usersRoutes)
app.register_blueprint(newsRoutes)
app.register_blueprint(CommentsRoutes)
app.register_blueprint(LoginRoute)

if __name__ == '__main__':
    app.run(debug = True)