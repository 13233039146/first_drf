from django.db import models

# Create your models here.
from django.db import models


class Department(models.Model):
    dept_name = models.CharField(max_length=20)
    dept_id = models.IntegerField()
    dept_peo_total = models.IntegerField()

    class Meta:
        db_table = 't_dept'
        verbose_name = '部门表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.dept_name


class Manager(models.Model):
    managerName = models.CharField(max_length=20)
    username = models.CharField(max_length=10)
    password = models.CharField(max_length=16)
    age = models.IntegerField()
    job = models.CharField(max_length=50)
    dept_id = models.ForeignKey(to='Department', on_delete=models.CASCADE)

    @property
    def depart(self):
        return self.dept_id.dept_id

    class Meta:
        db_table = 't_manager'
        verbose_name = '管理员表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.managerName


class Employee(models.Model):
    e_name = models.CharField(max_length=20)
    age = models.IntegerField()
    phone = models.CharField(max_length=11)
    dept_id = models.ForeignKey(to='Department', on_delete=models.CASCADE)

    class Meta:
        db_table = 't_employee'
        verbose_name = '员工表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.e_name
