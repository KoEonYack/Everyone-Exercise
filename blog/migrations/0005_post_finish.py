# Generated by Django 2.2.4 on 2019-08-18 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20190818_1414'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='finish',
            field=models.BooleanField(default=False),
        ),
    ]
