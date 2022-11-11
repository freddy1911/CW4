from dao.director import DirectorDAO
from dao.genre import GenreDAO
from dao.movie import MovieDAO
from dao.user import UserDAO
from servises.director import DirectorService
from servises.genre import GenreService
from servises.movie import MovieService
from servises.user import UserService
from setup_db import db

director_dao = DirectorDAO(db.session)
director_service = DirectorService(director_dao)

genre_dao = GenreDAO(db.session)
genre_service = GenreService(genre_dao)

movie_dao = MovieDAO(db.session)
movie_service = MovieService(movie_dao)

user_dao = UserDAO(db.session)
user_service = UserService(user_dao)
