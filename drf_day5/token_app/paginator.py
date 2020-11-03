from rest_framework.pagination import LimitOffsetPagination, PageNumberPagination


class MyPageNumberPagination(PageNumberPagination):
    # 指定每页分页的数量
    page_size = 2
    # 指定每页分页的最大数量
    max_page_size = 5
    # 指定前端修改每页分页数量的key
    page_size_query_param = "page_size"
    # 手机指定获取第几页的对象
    page_query_param = "page"


class MyLimitOffsetPagination(LimitOffsetPagination):
    # 默认获取每页的数量
    default_limit = 3
    # 指定前端获取每页数量的key
    limit_query_param = "limit"
    # 指定偏移开始的位置
    offset_query_param = "offset"
    # 指定每页获取的最大数量
    max_limit = 5