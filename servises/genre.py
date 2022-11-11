from dao.genre import GenreDAO


class GenreService:
    def __init__(self, dao: GenreDAO):
        self.dao = dao

    def get_all(self):
        return self.dao.get_all()

    def get_one(self, did):
        return self.dao.get_one(did)
