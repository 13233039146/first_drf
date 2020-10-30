from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from dangdang.models import Book
from dangdang.serializer import BookSerializer


class BookAPIView(APIView):
    def get(self, request, *args, **kwargs):

        book_id = request.query_params.get('id')
        if book_id:
            book = Book.objects.get(pk=book_id,is_delete=False)
            data = BookSerializer(book).data
            return Response({
                "status": 200,
                "message": "查询单个图书成功",
                "results": data,
            })
        else:
            all = Book.objects.filter(is_delete=False)
            book_all = BookSerializer(all, many=True).data
            return Response({
                "status": 200,
                "message": "查询所有图书成功",
                "results": book_all,
            })

    def post(self, request, *args, **kwargs):
        data = request.data
        if not data:
            return Response({
                'status': 400,
                'message': '数据传入有误'
            })
        if isinstance(data,dict):
            flag = False
        elif isinstance(data, list):
            flag = True
        else:
            return Response({
                'status':400,
                'msg':'格式错误'
            })
        # 反序列化
        ser = BookSerializer(data=data,many=flag)
        # 判断是否符合格式,不符合直接抛出异常
        ser.is_valid(raise_exception=True)
        book = ser.save()
        return Response({
            'status':200,
            'msg':'添加图书成功',
            'data':BookSerializer(book,many=flag).data
        })

    def delete(self, request, *args, **kwargs):
        id = kwargs.get('id')
        if id:
            ids = [id]
        else:
            ids = request.data.get('ids')


        res = Book.objects.filter(pk__in=ids, is_delete=False).update(is_delete=True)
        if res:
            return Response({
                "status": 200,
                "message": '删除成功'
            })

        return Response({
            "status": 400,
            "message": '删除失败'
        })

    # 修改一个
    def put(self, request, *args, **kwargs):

        request_data = request.data
        book_id = kwargs.get("id")
        try:
            b = Book.objects.get(pk=book_id)
        except Book.DoesNotExist:
            return Response({
                "status": 400,
                "message": '图书不存在'
            })

        # TODO 修改  需要自定关键字参数instance,不传入就是create方法,传入则调用update
        ser = BookSerializer(data=request_data, instance=b)
        ser.is_valid(raise_exception=True)
        ser.save()
        return Response({
            "status": 200,
            "message": '修改成功',
            "results": BookSerializer(b).data
        })

    # 修改一个的某些字段
    def patch(self, request, *args, **kwargs):

        request_data = request.data
        book_id = kwargs.get("id")

        try:
            book_obj = Book.objects.get(pk=book_id)
        except Book.DoesNotExist:
            return Response({
                "status": 400,
                "message": '图书不存在'
            })
        # 需要自定关键字参数instance  , 并且传入partial=True
        serializer = BookSerializer(data=request_data, instance=book_obj, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({
            "status": 200,
            "message": '修改成功',
            "results": BookSerializer(book_obj).data
        })
