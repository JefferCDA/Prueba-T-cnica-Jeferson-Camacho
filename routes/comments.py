from flask import Blueprint, request
from models.comments import Commets, commentsSchema
from utils.configdb import db
from flask_jwt_extended import jwt_required

CommentsRoutes = Blueprint('comments', __name__)

commetsSchema = commentsSchema()
manyCommentsSchema = commentsSchema(many = True)

@CommentsRoutes.route('/comments', methods = ['POST'])
@jwt_required
def setComments():
    try:
        news_id = request.json['news_id']
        user_id = request.json['user_id']
        comment = request.json['comment']
        
        newComment = Commets(news_id, user_id, comment)
        db.session.add(newComment)
        db.session.commit()

        return commetsSchema.jsonify(newComment)
    except Exception as e:
        print(e)
        return {'error': 'Error trying to set comments'}, 500
    
@CommentsRoutes.route('/comments', methods = ['GET'])
def getComments():
    try:
        allcomments = Commets.query.all()
        return manyCommentsSchema.jsonify(allcomments)
    
    except Exception as e:
        print(e)
        return {'error': 'Error trying to get comments'}, 500

@CommentsRoutes.route('/comments/<id>', methods = ['GET'])
def getComment(id):
    try:
        comment = Commets.query.filter_by(id = id).first()
        if comment is None:
            return {'error':'This news does not exist'}, 404
        return commetsSchema.jsonify(comment)
    
    except Exception as e:
        print(e)
        return {'error': 'Error trying to get comments'}, 500
    

@CommentsRoutes.route('/comments/<id>', methods = ['PUT'])
def updateComment(id):
    try:
        comment = Commets.query.filter_by(id = id).first()
        if comment is None:
            return {'error':'This news does not exist'}, 404
        newcomment = request.json['comment']
        comment.comment = newcomment
        db.session.commit()

        return commetsSchema.jsonify(comment)
    except Exception as e:
        print(e)
        return {'error': 'Error trying to get comments'}, 500