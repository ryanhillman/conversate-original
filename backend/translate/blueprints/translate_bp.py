from flask import Blueprint, render_template, jsonify, request
from ..extensions import db
from ..models import User, FlashCard

translate_bp = Blueprint('translate_bp', __name__)


@translate_bp.route('/users')
def index():
    return 'api'


@translate_bp.route('/api/users', methods=['GET', 'POST'])
def users():
    if request.method == 'GET':
        users = db.session.query(User).all()
        users_json = [x.serialize() for x in users]
        return (jsonify(users_json), 200) if users else (jsonify(error='No users'), 400)
    if request.method == 'POST':
        if request.json.get('email'):
            all_users = db.session.query(User).all()
            if request.json.get('user_name').lower() in [x.user_name.lower() for x in all_users] or request.json.get(
                    'email').lower() in [
                x.email.lower() for x in all_users]:
                return jsonify(error='User already exists'), 409
            else:
                new_user = User(request.json.get('email'), request.json.get('user_name'))
                db.session.add(new_user)
                db.session.commit()
                user_json = new_user.serialize()
                return jsonify({'message': 'success', 'data': user_json}), 201


@translate_bp.route('/api/users/<user_email>', methods=['GET', 'PUT', 'PATCH', 'DELETE'])
def user(user_email):
    user = db.session.query(User).filter_by(email=user_email).one_or_none()
    if user:
        if request.method == 'GET':
            return jsonify(user.serialize()), 200
        if request.method == 'PUT':
            if request.json.get('user_name'):
                all_users = db.session.query(User).all()
                if request.json.get('user_name') in [x.user_name for x in all_users]:
                    return jsonify(error='user_name already exists'), 409
                user.user_name = request.json.get('user_name')
                db.session.add(user)
                db.session.commit()
                return jsonify(user.serialize()), 204
        elif request.method == 'PATCH':
            user.score = user.score + 1
            db.session.commit()
        if request.method == 'DELETE':
            user_json = user.serialize()
            db.session.delete(user)
            db.session.commit()
            return jsonify({'message': 'success', 'data': user_json}), 204
    return jsonify(error='Unknown resource'), 404


@translate_bp.route('/api/questions', methods=['GET', 'POST'])
def questions():
    if request.method == 'GET':
        questions = db.session.query(FlashCard).all()
        questions_json = [x.serialize() for x in questions]
        return (jsonify(questions_json), 200) if questions else (jsonify(error='No questions'), 400)
    if request.method == 'POST':
        if request.json.get('question'):
            all_questions = FlashCard.query.all()
            if request.json.get('question').lower() in [x.question.lower() for x in all_questions]:
                return jsonify(error='Question already exists'), 409
            else:
                new_question = FlashCard(question=request.json.get('question'), choice_1=request.json.get('choice_1'), choice_2=request.json.get('choice_2'),
                choice_3=request.json.get('choice_3'), choice_4=request.json.get('choice_4'), correct_choice=request.json.get('correct_choice'))
                db.session.add(new_question)
                db.session.commit()
                question_json = new_question.serialize()
                return jsonify({'message': 'success', 'data': question_json}), 201


@translate_bp.route('/api/questions/<question_id>', methods=['GET', 'DELETE'])
def question(question_id):
    question = db.session.query(FlashCard).filter_by(id=question_id).one_or_none()
    if question:
        if request.method == 'GET':
            question_json = question.serialize()
            return jsonify(question_json), 200
        if request.method == 'DELETE':
            question_json = question.serialize()
            db.session.delete(question)
            db.session.commit()
            return jsonify({'message': 'success', 'data': question_json}), 204
    return jsonify(error='Unknown resource'), 404

@translate_bp.route('/api/users/check_username/<user_name>', methods=['GET'])
def check_username(user_name):
    all_users = db.session.query(User).all()
    if user_name.lower() in [x.user_name.lower() for x in all_users]:
        return jsonify(error='user_name taken'), 409
    return jsonify(message='Success'), 200
