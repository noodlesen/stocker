# Generated by Django 2.0.2 on 2018-03-18 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Motion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Take',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('motion', models.ForeignKey(on_delete='cascade', to='app.Motion')),
                ('project', models.ForeignKey(on_delete='cascade', to='app.Project')),
            ],
        ),
        migrations.RemoveField(
            model_name='footage',
            name='project',
        ),
        migrations.AddField(
            model_name='footage',
            name='take',
            field=models.ForeignKey(null=True, on_delete='cascade', to='app.Take'),
        ),
    ]
