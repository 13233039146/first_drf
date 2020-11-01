from rest_framework import serializers
from dangdang.models import Book, Author, Press

# 多对多
class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('author_name','age')


# 一对多查询
class PublishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Press
        fields = ('press_name', 'pic', 'address')


class BookSerializer(serializers.ModelSerializer):
    # publish = PublishSerializer()
    # 多对多需要指定many=True
    # authors = AuthorSerializer(many=True)
    class Meta:
        model = Book
        # 自定义字段只能出现在序列化
        # 默认序列化和反序列化都参与
        fields = ('book_name', 'price', 'authors')

        extra_kwargs = {
            "book_name": {
                "required": True,  # 必填字段
                "min_length": 2,  # 最小长度
                "error_messages": {
                    "required": "图书名必须提供",
                    "min_length": "图书名不能少于两个字符",
                }
            },

            # 'authors': {
            #     'write_only': True
            # },
            # 'publish': {
            #     'write_only': True
            # },
            #
            # 'pic': {
            #     'read_only': True
            # }

        }

    def validate(self, attrs):
        print(attrs)
        return attrs
