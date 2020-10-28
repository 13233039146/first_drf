from rest_framework.response import Response
from rest_framework.views import exception_handler as drf_eh
from rest_framework import status

def exception_handler(excp, content):
    # excp为异常描述，
    # content为 {'view': <teacher.views.TeacherAPIView object at 0x00000279B89CB9B0>, 'args': (), 'kwargs': {}, 'request': <rest_framework.request.Request object at 0x00000279B8BDB5F8>}
    error = '%s %s %s' % (excp, content['view'], content['request'].method)
    print(error)
    # 调用django提供的异常处理模块
    response = drf_eh(excp, content)
    if response is None:
        return Response({
            'error_msg': '亲爱的稍等，我们正在快马加鞭赶来~'
        },status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    return response