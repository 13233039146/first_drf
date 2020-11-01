from django.contrib import admin
from view_set import  models
admin.site.register(models.Manager)
admin.site.register(models.Employee)
admin.site.register(models.Department)
# Register your models here.
