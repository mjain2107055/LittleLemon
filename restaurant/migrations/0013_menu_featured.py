# Generated by Django 4.2.5 on 2023-10-21 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0012_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='featured',
            field=models.BooleanField(db_index=True, default=0),
            preserve_default=False,
        ),
    ]
