# Generated by Django 3.1.5 on 2021-01-17 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0002_auto_20210111_1110'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='priority',
            field=models.IntegerField(default=0),
        ),
    ]
