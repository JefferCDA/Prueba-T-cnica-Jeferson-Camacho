from utils.configdb import db, ma

class Comments(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    news_id = db.Column(db.Integer, db.ForeignKey('news.id') ,nullable=False)
    user_id = db.Column(db.Integer,db.ForeignKey ('users.id'),  nullable=False)
    comment = db.Column(db.String(255), nullable=False)

    def __init__(self, news_id, user_id, comment):
        self.news_id = news_id
        self.user_id = user_id
        self.comment = comment

class commentsSchema(ma.Schema):
    class Meta:
        fields = ('id','news_id', 'user_id', 'comment')