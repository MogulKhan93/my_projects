from django.db import models
import requests


class Rate(models.Model):

    class Meta:
        verbose_name = 'Валюта'
        verbose_name_plural = 'Курс валют'
        ordering = ('rate_name',)

    digital_code = models.IntegerField('Код цифровий')
    letter_code = models.CharField('Код літерний', max_length=3)
    rate_name = models.CharField('Назва валюти', max_length=40)
    official_rate = models.FloatField('Офіційний курс')

    
def get_rates():
    api = 'https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json'
    data = requests.get(api).json()
    return data


result0 = get_rates()
date_now = result0[0]['exchangedate']
