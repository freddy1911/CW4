from flask_restx import Resource, Namespace

from container import genre_service
from dao.models.genre import GenreSchema

genre_ns = Namespace('genres')


@genre_ns.route('/')
class GenreView(Resource):
    def get(self):
        genres = genre_service.get_all()
        result = GenreSchema(many=True).dump(genres)
        return result, 200


@genre_ns.route('/<int:gid>')
class GenreView(Resource):
    def get(self, gid):
        genre = genre_service.get_one(gid)
        result = GenreSchema().dump(genre)
        return result, 200