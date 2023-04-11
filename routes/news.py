from flask import Blueprint, request
from models.news import News, NewsSchema
from utils.configdb import db
from flask_jwt_extended import jwt_required

newsRoutes = Blueprint('news', __name__)

newsSchema = NewsSchema()
manyNewsSchema = NewsSchema(many = True)

@newsRoutes.route('/news', methods = ['POST'])
@jwt_required
def setNews():
    try:
        newsTitle = request.json['news_title']
        newsDescription = request.json['news_description']
        
        newNews = News(newsTitle, newsDescription)
        db.session.add(newNews)
        db.session.commit()

        return newsSchema.jsonify(newNews)
    except Exception as e:
        print(e)
        return {'error': 'Error trying to set news'}, 500

@newsRoutes.route('/news', methods = ['GET'])
def getNews():
    try:
        allNews = News.query.all()
        return manyNewsSchema.jsonify(allNews)
    
    except Exception as e:
        print(e)
        return {'error': 'Error trying to get news'}, 500

@newsRoutes.route('/news/<id>', methods = ['GET'])
def getNewsItem(id):
    try:
        news = News.query.filter_by(id = id).first()
        if news is None:
            return {'error':'This news does not exist'}, 404
        return newsSchema.jsonify(news)
    
    except Exception as e:
        print(e)
        return {'error': 'Error trying to get news'}, 500


@newsRoutes.route('/news/<id>', methods = ['PUT'])
def updateNewsItem(id):
    try:
        news = News.query.filter_by(id = id).first()
        if news is None:
            return {'error':'This news does not exist'}, 404
        
        newsTitle = request.json['news_title']
        newsDescription = request.json['news_description']

        news.news_title = newsTitle
        news.news_description = newsDescription
        
        db.session.commit()

        return newsSchema.jsonify(news)
    
    except Exception as e:
        print(e)
        return {'error': 'Error trying to update news'}, 500
    

@newsRoutes.route('/news/<id>', methods = ['DELETE'])
def deleteNewsItem(id):
    try:
        news = News.query.filter_by(id = id).first()
        if news is None:
            return {'error':'This news does not exist'}, 404
        
        db.session.delete(news)
        db.session.commit()

        return newsSchema.jsonify(news)
    
    except Exception as e:
        print(e)
        return {'error': 'Error trying to update news'}, 500
    