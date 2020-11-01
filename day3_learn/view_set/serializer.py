from rest_framework import serializers
from view_set.models import Manager, Department


class ManagerListSerializer(serializers.ListSerializer):

    def update(self, instance, validated_data):
        print(instance)  # 所有要修改的实例对象
        print(validated_data)  # 所要修改的对象的字段的值
        print(self.child)  # ManagerAPISerializer
        # 调用modelSerializer的updata方法,因为他可以单独更新,然后循环即可
        for index, value in enumerate(instance):
            self.child.update(value, validated_data[index])
        return instance


class DepartmentAPISerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ('dept_name',)


class ManagerAPISerializer(serializers.ModelSerializer):
    dept_id = DepartmentAPISerializer()

    class Meta:
        model = Manager
        list_serializer_class = ManagerListSerializer
        fields = ('managerName', 'username', 'password', 'age', 'job', 'dept_id', 'depart')

        extra_kwargs = {
            'password': {
                'required': True,
                'min_length': 6,
                'max_length': 16,
                'write_only': True,
                'error_messages': {
                    'min_length': '密码长度大于6',
                    'max_lenght': '密码长度小于16',
                    'required': '密码必须填写'
                }
            },
            'depart': {
                "read_only": True
            },
            'dept_id': {
                'write_only': True
            }
        }
