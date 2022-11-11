from sqlalchemy import desc

from dao.models.movie import Movie


class MovieDAO:
    def __init__(self, session):
        self.session = session

    def get_all(self):
        return self.session.query(Movie).all()

    def get_one(self, mid):
        return self.session.query(Movie).get(mid)

    def get_filter(self, filters):
        if filters.get('status') and filters.get('page'):
            page = int(filters.get('page'))
            return self.session.query(Movie).order_by(desc(Movie.yaer)).paginate(page=page, per_page=12).items
        elif filters.get('status'):
            return self.session.query(Movie).order_by(desc(Movie.year))
        elif filters.get('page'):
            page = int(filters.get('page'))
            return self.session.query(Movie).paginate(page=page, per_page=12).items
