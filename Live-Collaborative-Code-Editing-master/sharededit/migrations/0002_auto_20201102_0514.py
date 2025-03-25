# Generated by Django 3.1.2 on 2020-11-02 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sharededit', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='chatroom',
            name='is_occupied',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='chatroom',
            name='room_password',
            field=models.CharField(default='password', max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='chatroom',
            name='room_name',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]
