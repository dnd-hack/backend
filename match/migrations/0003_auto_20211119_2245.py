# Generated by Django 3.1 on 2021-11-19 22:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('match', '0002_auto_20211119_2205'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='gender',
            field=models.IntegerField(blank=True, choices=[(1, '여성'), (2, '남성')], null=True),
        ),
        migrations.AlterField(
            model_name='joinedmember',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='joined_member', to='match.group'),
        ),
    ]
