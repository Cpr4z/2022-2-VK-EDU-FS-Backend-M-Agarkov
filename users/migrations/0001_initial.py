# Generated by Django 4.1.2 on 2022-10-16 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=50, unique=True)),
                ('password', models.CharField(default='qwerty123', max_length=50)),
                ('reg_date', models.DateField(auto_now_add=True)),
                ('is_online', models.BooleanField(default=True)),
                ('is_photo', models.BooleanField(default=False)),
                ('user_info', models.CharField(max_length=200, unique=True)),
            ],
        ),
    ]
