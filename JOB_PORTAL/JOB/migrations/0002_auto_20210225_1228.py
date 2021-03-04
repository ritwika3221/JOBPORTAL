# Generated by Django 3.1.5 on 2021-02-25 06:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('JOB', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentuser',
            name='image',
        ),
        migrations.RemoveField(
            model_name='studentuser',
            name='type',
        ),
        migrations.AlterField(
            model_name='studentuser',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
