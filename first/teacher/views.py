from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView
from teacher.models import Teacher
from teacher.serializer import TeacherSerializer,TeacherDeserialezer
class TeacherAPIView(APIView):

    def get(self, request, *args, **kwargs):
        # 单独查询
        t_id = request.query_params.get('id')
        if t_id:
            t = Teacher.objects.filter(id=t_id)
            if t:
                t_serializer = TeacherSerializer(t[0]).data
                return Response({
                    'status': 200,
                    'messsage': '查询单个成功',
                    'result': t_serializer,
                })
        else:
            teachers = Teacher.objects.all()

            if teachers:
                # 多个值序列化需要传入many=True
                teachers_serializer = TeacherSerializer(teachers, many=True).data
                return Response({
                    'status': 200,
                    'messsage': '查询所有教师成功',
                    'result': teachers_serializer,
                })
        return Response({
            'status': 400,
            'messsage': '查询失败',
        })

    def post(self, request, *args, **kwargs):
        # 字典类型
        data = request.data
        if not isinstance(data, dict) or data == {}:
            return Response({
                "status": 400,
                "message": "参数错误",
            })
        deSerializer = TeacherDeserialezer(data=data)
        if deSerializer.is_valid():
            teacher = deSerializer.save()
            return Response({
                'status': 200,
                'message': '新增一条教师信息成功',
                # 拿出数据,渲染到前端,需要序列化
                'result': TeacherSerializer(teacher).data
            })
        else:
            return Response({
                "status": 400,
                "message": "添加失败",
                # 失败的信息会包含在 errors中
                "results": deSerializer.errors
            })


    def delete(self, request, *args, **kwargs):
        data = request.data

        t = Teacher.objects.filter(id=int(data['id']))
        temp = t[0]
        print(t)
        if t:
            t.delete()
            return Response({
                'status': 200,
                'message': '删除成功',
                'result':TeacherSerializer(temp).data
            })
        return Response({
            'status': 400,
            'message': '删除失败',
        })

