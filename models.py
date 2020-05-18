from flask_login import UserMixin

class User(UserMixin):
    pass

users = []

def query_user(user_id):
    users=get_user()
    print("users",users)
    for user in users:
        if user_id == user['id']:
            return user
    return None

def get_user():
    global users
    with open ('static/csv/users.csv','r',encoding='utf-8') as f:
        allusers=f.readlines()
        for item in allusers:
            item=str(item).split(',')
            idone={'id':item[0],'username':item[1],'password':str(item[2]).replace('\n','')}
            users.append(idone)
        return users

print(get_user())