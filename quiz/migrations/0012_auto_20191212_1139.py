# Generated by Django 2.2.6 on 2019-12-12 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0011_auto_20191212_1130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questionresponse',
            name='response_text',
            field=models.TextField(max_length=2000),
        ),
    ]
