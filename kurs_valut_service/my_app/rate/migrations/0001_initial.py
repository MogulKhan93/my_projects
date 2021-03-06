# Generated by Django 3.2.7 on 2021-09-18 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Rate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('digital_code', models.IntegerField(verbose_name='Код цифровий')),
                ('letter_code', models.CharField(max_length=3, verbose_name='Код літерний')),
                ('rate_name', models.CharField(max_length=40, verbose_name='Назва валюти')),
                ('official_rate', models.FloatField(verbose_name='Офіційний курс')),
            ],
        ),
    ]
