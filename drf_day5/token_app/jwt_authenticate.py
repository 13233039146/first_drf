import jwt
from rest_framework_jwt.authentication import BaseJSONWebTokenAuthentication, jwt_decode_handler
from rest_framework import exceptions


class JWTAuthen(BaseJSONWebTokenAuthentication):
    def authenticate(self, request):
        jwt_token = request.META.get('HTTP_AUTHORIZATION', None)

        token = self.parse_jwt(jwt_token)
        # 没解析到token什么都不做
        if token is None:
            return None
        try:
            payload = jwt_decode_handler(token)
        except jwt.ExpiredSignature:
            raise exceptions.AuthenticationFailed("签名过期")
        except:
            raise exceptions.AuthenticationFailed('非法用户')

        # 解析通过
        user = self.authenticate_credentials(payload)
        return user, token

    def parse_jwt(self, code):

        tokens = code.split()
        # 自定义规则
        if len(tokens) != 3 or tokens[0].lower() != "auth" or tokens[2].lower() != "jwt":
            return None
        return tokens[1]
