# Generated by Django 3.0.3 on 2020-09-01 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cryptonumjuggle', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdata',
            name='counter',
            field=models.IntegerField(default=0, max_length=100),
        ),
    ]
