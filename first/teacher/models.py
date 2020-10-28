from django.db import models


# Create your models here.
class Teacher(models.Model):
    gender_choices = [
        (0, 'male'),
        (1, 'female'),
        (2, 'secret'),
    ]
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    gender = models.SmallIntegerField(choices=gender_choices, default=2)
    job = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    pic = models.ImageField(upload_to='image/',default='image/1.jpg')

    class Meta():
        db_table = 'teacher'
        verbose_name = '教师表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
