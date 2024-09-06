import os

class Constants:
    try:
        login = os.getenv('AUTH_LOGIN')
        password = os.getenv('AUTH_PASSWORD')
    except KeyError:
        print("Логин не прошёл")