# Generated by Django 2.0.2 on 2018-03-18 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20180318_1405'),
    ]

    operations = [
        migrations.AddField(
            model_name='take',
            name='description',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='take',
            name='name',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
