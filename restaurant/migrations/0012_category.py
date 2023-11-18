# Generated by Django 4.2.5 on 2023-10-21 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0011_rename_name_booking_model_first_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField()),
                ('title', models.CharField(db_index=True, max_length=255)),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
    ]