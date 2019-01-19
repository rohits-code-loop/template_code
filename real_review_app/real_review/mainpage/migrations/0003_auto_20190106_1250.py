# Generated by Django 2.1 on 2019-01-06 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0002_auto_20190102_0721'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='id',
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.CharField(max_length=30, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='usrID',
            field=models.CharField(max_length=30, primary_key=True, serialize=False),
        ),
    ]
