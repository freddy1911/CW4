import base64
import hashlib

from constants import PWD_HASH_SALT, PWD_HASH_ITERATIONS
from dao.user import UserDAO


class UserService:
    def __init__(self, dao: UserDAO):
        self.dao = dao

    def get_one(self, uid):
        return self.dao.get_one(uid)

    def create(self, data):
        password = data.get('password')
        hash_pass = self.get_hash(password)
        data['password'] = hash_pass

        return self.dao.create(data)

    def get_hash(self, password):
        hashed_password = hashlib.pbkdf2_hmac(
            'sha256',
            password.encode('utf-8'),
            PWD_HASH_SALT,
            PWD_HASH_ITERATIONS)

        return base64.b64encode(hashed_password)

    def get_by_email(self, email):
        return self.dao.get_by_email(email)