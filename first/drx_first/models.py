from django.db import models


# Create your models here.
class User(models.Model):
    gender_choice = (
        (0, 'male'),
        (1, 'female'),
    )
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    gender = models.SmallIntegerField(choices=gender_choice, default=0)
    age = models.IntegerField()

    class Meta:
        db_table = 'user_drf'
        verbose_name = '用户表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username
