from flask import request, jsonify
import jwt
import re
from config import SECRET, ALGORITHM


def login_validate(func):
    def wrapper(self, request, *args, **kwargs):
        try:
            token = request.headers.get('Authorization', None)
            payload = jwt.decode(token, SECRET['secret'], ALGORITHM['algorithm'])
            return func(self, payload, *args, **kwargs)
        except Exception as e:
            return jsonify({'message': f'{e}'}), 400
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
