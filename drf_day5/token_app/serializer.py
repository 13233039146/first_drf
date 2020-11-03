import re

from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from rest_framework_jwt.settings import api_settings

from demo.models import User

# 信息->载荷
from token_app.models import Phone

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
# 载荷->token
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER


class UserSerializer(ModelSerializer):
    account = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ["account", "password", "username", "phone", "email"]
        extra_kwargs = {
            "username": {
                "read_only": True
            },
            "phone": {
                "read_only": True
            },
            "email": {
                "read_only": True
            },
        }

    def validate(self, attrs):
        account = attrs.get('account')
        password = attrs.get('password')

        if re.match(r'1[3-9][0-9]{9}', account):
            user = User.objects.filter(phone=account).first()
        elif re.match(r'.+@.+', account):
            user = User.objects.filter(email=account).first()
        else:
            user = User.objects.filter(username=account).first()

        # 如果用户格式正确并且密码正确
        if user and user.check_password(password):
            # 通过信息生成载荷
            payload = jwt_payload_handler(user)
            # 通过载荷生成token
            token = jwt_encode_handler(payload)
            # 通过serializer传递到视图
            self.user_obj = user
            self.token = token

        return attrs
class PhonerModelSerializer(ModelSerializer):
    class Meta:
        model = Phone
        fields = ("name", "price", "size", "brand")