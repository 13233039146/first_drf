from django.db import transaction
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from drx_first.models import User


# Create your views here.
class UserAPIView(APIView):
    def get(self, request, *args, **kwargs):
        # 查询单个用户
        user_id = kwargs.get('id')
        if user_id:
            print('单独查询')
            user = User.objects.filter(id=user_id).values('username', 'password', 'gender', 'age')
            if user:
                return Response({
                    'status': 200,
                    'message': '查询单个用户成功',
                    'result': user
                })
            # 查询多个用户
        else:
            print('多个查询')
            users = User.objects.all().values('username', 'password', 'gender', 'age')
            if users:
                return Response({
                    'status': 200,
                    'message': '查询所有用户成功',
                    'result': list(users)
                })
        return Response({
            'status': 400,
            'message': '查询失败',
        })

    # 增加用户
    def post(self, request, *args, **kwargs):
        # data = request.data
        # print(data)
        username = request.POST.get('username')
        password = request.POST.get('password')
        gender = request.POST.get('gender')
        age = request.POST.get('age')
        try:
            with transaction.atomic():
                user = User.objects.create(
                    username=username,
                    password=password,
                    gender=gender,
                    age=age,
                )
                result = {
                    'username': user.username,
                    'gender': user.gender,
                    'age': user.age,
                }
                return Response({
                    'status': 200,
                    'message': '成功添加一条用户信息',
                    'result': result,
                })
        except:
            print('添加出错')
            return Response({
                'status': 400,
                'message': '添加用户失败',
            })

    # 删除单个用户
    def delete(self, request, *args, **kwargs):
        id = kwargs.get('id')
        user = User.objects.filter(id=id)
        if user:
            user.delete()
            return Response({
                'status': 200,
                'message': '删除成功',
            })
        return Response({
            'status': 400,
            'message': '删除失败',
        })
