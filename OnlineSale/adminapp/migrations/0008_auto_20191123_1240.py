# Generated by Django 2.2.3 on 2019-11-23 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0007_customerdetails'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerdetails',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]
