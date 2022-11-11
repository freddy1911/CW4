from dao.models.user import User


class UserDAO:
    def __init__(self, session):
        self.session = session

    def create(self, data):
        new_user = User(**data)
        self.session.add(new_user)
        self.session.commit()
        return new_user

    def get_one(self, uid):
        return self.session.query(User).get(uid)

    def get_by_email(self, email: str):
        user = self.session.query(User).filter(User.email == email.lower()).first()

        return user

    def update(self, user_data):
        user = self.get_by_email(user_data.get('email'))

        user.name = user_data.get('name')
        user.surname = user_data.get('surname')
        user.favorite_genre_id = user_data.get('favorite_genre_id')

        self.session.add(user)
        self.session.commit()
