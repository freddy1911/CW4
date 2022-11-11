from flask import request
from flask_restx import Namespace, Resource
from servises.auth import generate_token, approve_refresh_token

from container import user_service

auth_ns = Namespace('auth')


@auth_ns.route('/register')
class AuthView(Resource):
    def post(self):
        data = request.json
        email = data.get("email")
        password = data.get("password")

        if None in [email, password]:
            return '', 400
        user_service.create(data)
        return '', 201


@auth_ns.route('/login')
class AuthView(Resource):
    def post(self):
        email = request.json.get('email')
        password = request.json.get('password')
        tokens = generate_token(email, password)
        return tokens, 201

    def put(self):
        data = request.json
        refresh_token = data.get('refresh_token')
        tokens = approve_refresh_token(refresh_token)

        return tokens, 201
