from flask import request, jsonify
import jwt
import re
from config import SECRET, ALGORITHM
from connection import get_connection


def login_validate(func):
    def wrapper(self, request, *args, **kwargs):
        conn = get_connection()
        token = request.headers.get('Authorization', None)
        if token is None:
            return jsonify({'message': 'TOKEN_DOES_NOT_EXIST'}, 403)
        try:
            decode = jwt.decode(token, SECRET['secret'], ALGORITHM['algorithm'])
            user = self.user_dao.get_seller_info(conn, decode)
            request.user_id = user['user_id']
            request.class_id = user['class_id']
            return func(self, request, *args, **kwargs)
        except Exception as e:
            return jsonify({'message': 'error {}'.format(e)}), 400
        finally:
            conn.close()
    return wrapper


def password_validate(value):
    if not re.match(r'^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,20}$', value):
        return True


def email_validate(value):
    if not re.match(r'^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', value):
        return True


def phone_number_validate(value):
    if not re.match(r'\d{2,3}-\d{3,4}-\d{4}', value):
        return True
