import hmac
from resources.user import UserModule
    

def authenticate(username, password):
    print("This is from authenticate username: ", username)
    print("This is from authenticate password: ", password)
    user = UserModule.findUsername(username)
    print("This is from authenticate user object: ", user)
    if user and hmac.compare_digest(user.password, password):
        return user

def identity(payload):
    user_id = payload['identity']
    print("This is from identity method: ", user_id)
    return UserModule.findId(user_id)