# Generated by Django 2.2.6 on 2019-11-26 22:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0009_auto_20191126_1727'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quizresponse',
            name='id_number',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='quizresponse',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
