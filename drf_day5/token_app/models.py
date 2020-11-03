from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class Phone(models.Model):
    name = models.CharField(max_length=50,unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    size = models.CharField(max_length=30)
    brand = models.CharField(max_length=10, verbose_name="品牌")

    class Meta:
        db_table = 'phone'
        verbose_name = '手机'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name