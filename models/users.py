from utils.configdb import db, ma 
from werkzeug.security import generate_password_hash

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_fullname = db.Column(db.String(255), nullable=False)
    user_email = db.Column(db.String(255), nullable=False, unique=True)
    user_password = db.Column(db.String(255), nullable = False)
    user_address = db.Column(db.String(255), nullable = False)
    user_phone = db.Column(db.String(255), nullable =False)
    user_date = db.Column(db.String(255), nullable = False)

    def __init__(self, user_fullname, user_email, user_password, user_address, user_phone, user_date):
        self.user_fullname = user_fullname
        self.user_email = user_email
        self.user_password = generate_password_hash(user_password)
        self.user_address = user_address
        self.user_phone = user_phone
        self.user_date = user_date


class UsersSchema(ma.Schema):
    class Meta:
        fields = ('id', 'user_fullname', 'user_email', 'user_address', 'user_phone', 'user_date')