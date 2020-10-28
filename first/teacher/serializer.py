from rest_framework import serializers

from first.settings import MEDIA_URL
from teacher.models import Teacher


class TeacherSerializer(serializers.Serializer):
    name = serializers.CharField()
    age = serializers.IntegerField()
    # gender = serializers.IntegerField()
    job = serializers.CharField()
    phone = serializers.CharField()
    # pic = serializers.ImageField()

    # 自定义自段
    gender = serializers.SerializerMethodField()

    def get_gender(self, obj):
        # gender 值是choices类型 get_字段名_display直接访问值
        return obj.get_gender_display()

    pic = serializers.SerializerMethodField()

    def get_pic(self, obj):
        url ='%s%s%s' % ('http://127.0.0.1:8000/',MEDIA_URL,str(obj.pic))
        return url

class TeacherDeserialezer(serializers.Serializer):
    name = serializers.CharField(min_length=1,
                                 max_length=4,error_messages={
            'min_length':'长度太短,请输入正确的名字',
            'max_length':'长度太长,请输入正确的名字',
        })
    age = serializers.IntegerField(max_value=90,min_value=18)
    gender = serializers.IntegerField(max_value=2,min_value=0)
    job = serializers.CharField()
    phone = serializers.CharField(max_length=11,min_length=11)
    # pic = serializers.ImageField()

    def create(self, validated_data):
        return Teacher.objects.create(**validated_data)