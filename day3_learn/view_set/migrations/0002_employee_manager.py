# Generated by Django 2.0.6 on 2020-10-30 09:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('view_set', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('e_name', models.CharField(max_length=20)),
                ('age', models.IntegerField()),
                ('phone', models.CharField(max_length=11)),
                ('dept_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='view_set.Department')),
            ],
            options={
                'verbose_name': '员工表',
                'verbose_name_plural': '员工表',
                'db_table': 't_employee',
            },
        ),
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('managerName', models.CharField(max_length=20)),
                ('username', models.CharField(max_length=10)),
                ('password', models.CharField(max_length=16)),
                ('age', models.IntegerField()),
                ('job', models.CharField(max_length=50)),
                ('dept_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='view_set.Department')),
            ],
            options={
                'verbose_name': '管理员表',
                'verbose_name_plural': '管理员表',
                'db_table': 't_manager',
            },
        ),
    ]