import jwt
from fastapi import HTTPException, Security, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from passlib.context import CryptContext
from datetime import datetime, timedelta



class AuthHandler():
    security = HTTPBearer()
    password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
    secret = "SECRET"


    def get_password_hash(self, password):
        return self.password_context.hash(password)



    def verify_password_hash(self,plain_password, passwordhashed):
        return self.password_context.verify(plain_password, passwordhashed)
    
    
    
    
    def encode_token(self, user_id):
        payload ={
            'exp': datetime.utcnow() +timedelta(days=0, minutes=5),
            'iat':datetime.utcnow(),
            'sub': user_id
        }
        return jwt.encode(
            payload,
            self.secret,
            algorithms ='HS256'
        )


    
    def decode_token(self, token):
        try:
            payload = jwt.decode(token, self.secret, algorithms=['HS256'])
            return payload['sub']
        except jwt.ExpiredSignatureError:
            return HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Signature has expired')
        except jwt.InvalidTokenError as e:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Invalid Token')
        


    def oauth_wrapper(self, oauth: HTTPAuthorizationCredentials = Security(security)):
        return self.decode_token(oauth.credentials)