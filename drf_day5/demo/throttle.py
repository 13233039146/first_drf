from rest_framework.throttling import SimpleRateThrottle


# 继承SimpleRateThrottle类
class SendMsgRate(SimpleRateThrottle):
    # 重新定义scope 默认为None
    scope = 'whj'

    # 重写该方法
    def get_cache_key(self, request, view):
        phone = request.query_params.get('phone')
        if not phone:
            return None
        return "ok"
