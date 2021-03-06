# Generated by Django 2.0.6 on 2020-10-28 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
                ('gender', models.SmallIntegerField(choices=[(0, 'male'), (1, 'female'), (2, 'secret')], default=2)),
                ('job', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': '教师表',
                'verbose_name_plural': '教师表',
                'db_table': 'teacher',
            },
        ),
    ]
