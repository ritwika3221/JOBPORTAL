# Generated by Django 3.1.5 on 2021-03-02 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('JOB', '0009_jobapplied'),
    ]

    operations = [
        migrations.AddField(
            model_name='reqruiteruser',
            name='email',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='studentuser',
            name='email',
            field=models.CharField(default='', max_length=50),
        ),
    ]
