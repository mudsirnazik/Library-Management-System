def authenticate(username, password, user_db):
    return user_db.get(username) == password
