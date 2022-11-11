from flask_restx import Resource, Namespace
from flask import request
from container import movie_service
from dao.models.movie import MovieSchema

movie_ns = Namespace('movies')


@movie_ns.route('/')
class MovieView(Resource):
    def get(self):

        page = request.args.get('page')
        status = request.args.get('status')

        filters = {
            "page": page,
            "status": status
                  }

        movies = movie_service.get_all(filters)
        result = MovieSchema(many=True).dump(movies)
        return result, 200


@movie_ns.route('/<int:mid>')
class MovieView(Resource):
    def get(self, mid):
        try:
            movie = movie_service.get_one(mid)
            result = MovieSchema().dump(movie)
            return result, 200
        except Exception as e:
            return e

