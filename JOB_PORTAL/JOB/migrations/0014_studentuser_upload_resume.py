# Generated by Django 3.1.5 on 2021-03-03 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('JOB', '0013_auto_20210303_1201'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentuser',
            name='upload_resume',
            field=models.FileField(default='', upload_to='documents'),
        ),
    ]
