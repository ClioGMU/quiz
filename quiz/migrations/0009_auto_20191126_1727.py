# Generated by Django 2.2.6 on 2019-11-26 22:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0008_auto_20191126_1720'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quizresponse',
            name='id_number',
            field=models.IntegerField(default='123'),
        ),
        migrations.AlterField(
            model_name='quizresponse',
            name='name',
            field=models.CharField(default='None', max_length=100),
        ),
    ]
