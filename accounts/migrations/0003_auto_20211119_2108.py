# Generated by Django 3.1 on 2021-11-19 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20211119_2102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='nickname',
            field=models.CharField(blank=True, max_length=15, null=True, unique=True),
        ),
    ]
