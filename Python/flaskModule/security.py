import hmac
from resources.user import UserModule


def authenticate(username, password):
    user = UserModule.findUsername(username)
    if user and hmac.compare_digest(user.password, password):
        print("This is from the authenticate function: ", user)
        return user


def identity(payload):
    user_id = payload['identity']
    return UserModule.findId(user_id)