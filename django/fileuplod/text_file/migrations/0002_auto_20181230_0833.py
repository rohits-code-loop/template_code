# Generated by Django 2.1 on 2018-12-30 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('text_file', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profilephotos',
            name='url',
            field=models.ImageField(upload_to=''),
        ),
    ]