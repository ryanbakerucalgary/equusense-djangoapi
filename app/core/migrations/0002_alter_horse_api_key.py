# Generated by Django 3.2.18 on 2023-03-25 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='horse',
            name='api_key',
            field=models.CharField(default='pmyUdGkMKwpb', max_length=12, unique=True),
        ),
    ]
