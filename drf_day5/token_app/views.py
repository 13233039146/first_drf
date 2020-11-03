from django.shortcuts import render

# Create your views here.
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from token_app.jwt_authenticate import JWTAuthen
from token_app.models import Phone
from token_app.serializer import UserSerializer
from token_app.serializer import PhonerModelSerializer
from rest_framework.filters import SearchFilter, OrderingFilter
from token_app.paginator import MyLimitOffsetPagination, MyPageNumberPagination
from token_app.filter import PhoneFilter

#  用户登录成功,则进行查询
class GetInfo(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthen]

    def get(self, request, *args, **kwargs):
        return Response('token is ok, query going')


# 多种方式登录
class LoginManyAPIView(APIView):
    # 1 禁用权限和认证组件
    # 2 获取前端参数
    # 3 校验
    # 4 签发token 返回到前端
    permission_classes = ()
    authentication_classes = ()

    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response({
            'token': serializer.token,
            'user': UserSerializer(serializer.user_obj).data
        })


class FilterPhone(ListAPIView):
    queryset = Phone.objects.all()
    serializer_class = PhonerModelSerializer
    # 配置要使用的过滤器类

    # 第三个是Django-filter需要的类
    filter_backends = [SearchFilter, OrderingFilter, DjangoFilterBackend]

    # 指定查询条件字段
    search_fields = ['name', 'size', 'brand']
    # ordering = ['price']
    # ordering不指定也可以使用

    pagination_class = MyPageNumberPagination
    # pagination_class = MyLimitOffsetPagination
    filter_class = PhoneFilter