# Generated by Django 3.1.5 on 2021-03-03 06:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('JOB', '0012_auto_20210303_1158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobapplied',
            name='studentuser',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='JOB.studentuser'),
        ),
    ]
