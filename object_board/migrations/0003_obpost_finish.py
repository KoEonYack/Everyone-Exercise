# Generated by Django 2.2.4 on 2019-08-22 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('object_board', '0002_objcomment_obpost'),
    ]

    operations = [
        migrations.AddField(
            model_name='obpost',
            name='finish',
            field=models.BooleanField(default=False),
        ),
    ]
