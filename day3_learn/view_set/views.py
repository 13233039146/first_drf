from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from view_set.models import Manager
from view_set import serializer
from rest_framework.generics import GenericAPIView
from rest_framework import generics
from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.viewsets import ViewSet


# 基于APIView的视图开发
class ManagerApiView(APIView):
    def get(self, rquest, *args, **kwargs):
        id = kwargs.get('id')
        print(id)
        if id:
            try:
                m = Manager.objects.get(id=id)
                ser = serializer.ManagerAPISerializer(m).data
                return Response({
                    'status': status.HTTP_200_OK,
                    'msg': '查到一条管理者信息',
                    'data': ser
                })
            except:
                return Response({
                    'status': status.HTTP_400_BAD_REQUEST,
                    'msg': '查无此人'
                })
        else:
            ms = Manager.objects.all()
            ser = serializer.ManagerAPISerializer(ms, many=True).data
            return Response({
                'status': status.HTTP_200_OK,
                'msg': '查到了所有管理员信息',
                'data': ser
            })

    def post(self, request, *args, **kwargs):
        data = request.data
        if data:
            if isinstance(data, dict):
                flag = False
            elif isinstance(data, list):
                flag = True
            ser = serializer.ManagerAPISerializer(data=data, many=flag)
            ser.is_valid(raise_exception=True)
            result = ser.save()
            return Response({
                'status': status.HTTP_200_OK,
                'msg': '添加成功',
                'data': serializer.ManagerAPISerializer(result).data
            })
        else:
            return Response({
                'status': status.HTTP_400_BAD_REQUEST,
                'msg': '添加失败'
            })

    def patch(self, request, *args, **kwargs):
        data = request.data
        id = kwargs.get('id')
        if id and isinstance(data, dict):
            ids = [id]
            data = [data]
        elif not id and isinstance(data, list):
            ids = []
            for item in data:
                # 取出id 没有则置None
                pk = item.pop('id', None)
                if pk:
                    ids.append(pk)
                else:
                    return Response({
                        "status": status.HTTP_400_BAD_REQUEST,
                        "message": "id不存在",
                    })
        else:
            return Response({
                "status": status.HTTP_400_BAD_REQUEST,
                "message": "参数格式有误",
            })
        m_list = []
        value = []  # 要修改的值
        for index, pk in enumerate(ids):
            try:
                m_obj = Manager.objects.get(pk=pk)
                m_list.append(m_obj)
                value.append(data[index])
            except Manager.DoesNotExist:
                continue
        ser = serializer.ManagerAPISerializer(data=value, instance=m_list, partial=True, many=True)
        ser.is_valid(raise_exception=True)
        ser.save()
        return Response({
            "status": status.HTTP_200_OK,
            "message": "修改成功",
        })

    def delete(self, request, *args, **kwargs):
        m_id = kwargs.get('id')
        if m_id:
            ids = [m_id]
        else:
            ids = request.data.get('ids')
        # res = Manager.objects.filter(pk__in=ids).delete()


# 基于Generic和mixin开发视图   Generic三大方法 + mxin五大模块
class ManagerGenAPIView(GenericAPIView, mixins.CreateModelMixin,
                        mixins.RetrieveModelMixin,
                        mixins.ListModelMixin,
                        mixins.DestroyModelMixin,
                        mixins.UpdateModelMixin):
    lookup_field = 'id'
    queryset = Manager.objects.filter()
    serializer_class = serializer.ManagerAPISerializer

    def get(self, request, *args, **kwargs):
        if 'id' in kwargs:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)


# 基于generic(generic继承了mixin下的五大工具包+Generic的三大方法) 视图开发
class ManagergenAPIView(generics.ListAPIView):
    queryset = Manager.objects.all()
    serializer_class = serializer.ManagerAPISerializer
    lookup_field = "id"
    # 单独查询和多个查询不能同时存在


# 基于viewsets视图开发
class ManagerViewsetAPIView(ViewSet):
    def registe(self, request, *args, **kwargs):
        data = request.data
        if data:
            name = data.get('username')
            pwd = data.get('password')
            if name and pwd:
                db_name = Manager.objects.filter(username=name)
                if db_name:
                    return Response({
                        'status': status.HTTP_400_BAD_REQUEST,
                        'msg': '用户名已存在'
                    })
                else:
                    ser = serializer.ManagerAPISerializer(data=data)
                    ser.is_valid(raise_exception=True)
                    result = ser.save()
                    return Response({
                        'status': status.HTTP_200_OK,
                        'msg': '注册成功',
                        'data': serializer.ManagerAPISerializer(result).data
                    })
            else:
                return Response({
                    'status': status.HTTP_400_BAD_REQUEST,
                    'msg': '请输入用户名和密码'
                })

        else:
            return Response({
                'status': status.HTTP_400_BAD_REQUEST,
                'msg': '注册格式错误'
            })

    def login(self, request, *args, **kwargs):
        data = request.data
        if data:
            m = Manager.objects.filter(username=data.get('username'), password=data.get('password'))
            if m:
                m_data = serializer.ManagerAPISerializer(m[0]).data
                return Response({
                    'stauts': status.HTTP_200_OK,
                    'msg': '登录成功',
                    'data': m_data
                })
            else:
                return Response({
                    'status': status.HTTP_400_BAD_REQUEST,
                    'msg': '用户名或密码错误'
                })
        else:
            return Response({
                'status': status.HTTP_400_BAD_REQUEST,
                'msg': '登录信息错误'
            })
