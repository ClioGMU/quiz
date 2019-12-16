# Generated by Django 2.2.8 on 2019-12-16 00:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0014_auto_20191214_1617'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='notes_for_question',
            field=models.TextField(blank=True, max_length=6000),
        ),
        migrations.AlterField(
            model_name='questionresponse',
            name='response_text',
            field=models.TextField(max_length=6000, null=True),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='date_created',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='quizresponse',
            name='attempt_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
