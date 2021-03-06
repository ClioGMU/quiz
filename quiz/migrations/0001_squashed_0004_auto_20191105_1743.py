# Generated by Django 2.2.5 on 2019-11-12 17:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    replaces = [('quiz', '0001_initial'), ('quiz', '0002_auto_20191104_1345'), ('quiz', '0003_auto_20191105_1713'), ('quiz', '0004_auto_20191105_1743')]

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('date_created', models.DateField(auto_now=True)),
                ('directions_and_introductory_text', models.TextField(max_length=5000)),
                ('primary_source_text', models.TextField(max_length=20000)),
                ('message', models.TextField(blank=True, max_length=2000)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Quiz',
                'verbose_name_plural': 'Quizzes',
            },
        ),
    ]
