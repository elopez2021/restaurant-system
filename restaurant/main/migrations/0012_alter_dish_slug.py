# Generated by Django 3.2.9 on 2021-12-01 00:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_dish_is_featured'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dish',
            name='slug',
            field=models.SlugField(max_length=400, null=True),
        ),
    ]
