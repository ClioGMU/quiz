# Generated by Django 2.2.5 on 2019-11-05 22:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('quiz', '0004_auto_20191105_1743'),
    ]

    operations = [
        migrations.CreateModel(
            name='Respondent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quiz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.Quiz')),
            ],
        ),
    ]
