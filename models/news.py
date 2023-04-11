from utils.configdb import db, ma

class News(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    news_title = db.Column(db.String(255), nullable=False)
    news_description = db.Column(db.String(255), nullable=False)

    def __init__(self, news_title, news_description):
        self.news_title = news_title
        self.news_description = news_description

class NewsSchema(ma.Schema):
    class Meta:
        fields = ('id','news_title', 'news_description')