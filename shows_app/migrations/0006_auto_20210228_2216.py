# Generated by Django 2.2 on 2021-03-01 03:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shows_app', '0005_auto_20210228_2134'),
    ]

    operations = [
        migrations.AlterField(
            model_name='show',
            name='release_date',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
