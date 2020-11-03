from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from demo.models import User
from demo.permissioner import MyPermission
from demo.throttle import SendMsgRate


class UserAPIView(APIView):
    def get(self, request, *args, **kwargs):
        user = User.objects.first()
        print("用户:", user)
        print("用户角色:", user.groups.first())
        print("用户权限:", user.user_permissions.first())

        return Response({
            'status': status.HTTP_200_OK,
            'msg': '查询成功',
        })


class UserPermissionAPI(APIView):
    # 局部配置
    permission_classes = [MyPermission]
    # 局部配置
    throttle_classes = [SendMsgRate]
    def get(self, request, *args, **kwargs):
        print("这是一个只读的请求")
        return Response("只读")

    def post(self, request, *args, **kwargs):
        print("这是一个写请求")
        return Response("写!")
