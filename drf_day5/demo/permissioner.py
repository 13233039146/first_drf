from rest_framework.permissions import BasePermission

# 继承BasePermission
from demo.models import User


class MyPermission(BasePermission):

    # 重写has_permission
    def has_permission(self, request, view):
        # 只读: 三种方法
        if request.method in ("GET","HEAD","OPTIONS"):
            return True

        # 写操作
        username = request.data.get('username')
        # 从数据库中对比
        user = User.objects.filter(username=username).first()
        # 用户有权限返回True
        if user: return True
        # 无权限返回False
        return False
