# Generated by Django 4.2.6 on 2023-10-12 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='inventory',
            field=models.SmallIntegerField(default=12),
            preserve_default=False,
        ),
    ]
