# Generated by Django 2.2 on 2019-04-11 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mascota', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mascota',
            name='votos',
            field=models.IntegerField(default=0),
        ),
    ]
