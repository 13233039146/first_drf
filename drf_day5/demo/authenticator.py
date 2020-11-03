from rest_framework.authentication import BaseAuthentication
from rest_framework import exceptions

# 继承BaseAuthentication类
from demo.models import User


class MyAuthentication(BaseAuthentication):

    # 重写authenticate方法
    def authenticate(self, request):
        # 获取认证信息,使用META和HTTP_AUTHORIZATION
        authen = request.META.get('HTTP_AUTHORIZATION', None)
        print(authen)

        # 没有信息为游客
        if authen is None:
            return None
        # 校验规则
        users = ['whj', 'wyj', 'wzj', 'wanghaojei']
        # 有信息
        au_sp = authen.split()
        # 同时都不满足长度为2且第一个字符是whj_auth
        if not (len(au_sp) == 2 and au_sp[0].lower() == 'whj_auth'):
            raise exceptions.AuthenticationFailed("认证失败,格式错误")
        if au_sp[1] not in users:
            raise exceptions.AuthenticationFailed("认证失败")
        # 数据库校验
        print(au_sp[1])
        auth_user = User.objects.filter(username=au_sp[1]).first()

        if not auth_user:
            raise exceptions.AuthenticationFailed('用户不存在或者已经删除了')

        # 返回一个元组(user,None)
        return auth_user, None
