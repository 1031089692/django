# Generated by Django 2.0.5 on 2018-12-01 01:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0003_auto_20181118_0151'),
    ]

    operations = [
        migrations.CreateModel(
            name='ActionApi',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('action_name', models.CharField(max_length=50)),
                ('api_path', models.CharField(max_length=50)),
                ('params', models.TextField(max_length=200)),
                ('headers', models.TextField(max_length=200)),
                ('abandon_flag', models.IntegerField(default=1)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.CharField(max_length=20)),
                ('updated_by', models.CharField(max_length=20)),
                ('descriptions', models.TextField(max_length=200)),
            ],
        ),
    ]
