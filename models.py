from flask_login import UserMixin

class User(UserMixin):
    pass

users = [
    {'id':'donghuibiao', 'username': 'donghuibiao', 'password': '123456'},
    {'id':'gaohao', 'username': 'gaohao', 'password': '123456'}
]

def query_user(user_id):
    for user in users:
        if user_id == user['id']:
            return user
