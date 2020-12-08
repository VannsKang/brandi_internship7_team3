import jwt
import re

from flask      import request, jsonify, g
from config     import SECRET, ALGORITHM
from functools  import wraps


def login_validate(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        token = request.headers.get('Authorization', None)
        if token is None:
            return jsonify({'message': 'TOKEN_DOES_NOT_EXIST'}), 403

        try:
            payload = jwt.decode(token, SECRET['secret'], ALGORITHM['algorithm'])
            user_id = payload['id']
            g.user_id = user_id

            return func(*args, **kwargs)

        except Exception as e:
            return jsonify({'message': format(e)}), 400
    return decorated_function


def password_validate(value):
    if not re.match(r'^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,20}$', value):
        return True


def email_validate(value):
    if not re.match(r'^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', value):
        return True


def phone_number_validate(value):
    if not re.match(r'\d{2,3}-\d{3,4}-\d{4}', value):
        return True
