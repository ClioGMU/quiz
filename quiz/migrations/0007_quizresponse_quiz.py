# Generated by Django 2.2.5 on 2019-11-19 18:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0006_auto_20191112_1307'),
    ]

    operations = [
        migrations.AddField(
            model_name='quizresponse',
            name='quiz',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='quiz.Quiz'),
            preserve_default=False,
        ),
    ]
