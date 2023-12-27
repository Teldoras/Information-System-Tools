from django.db import models
import datetime

# Create your models here.

# создание модели данных класса Model

class SearchingUsers(models.Model):
    # модель имеет одно текстовое поле
    ByName = models.CharField(max_length=100)
    ByDate = models.DateField(default=datetime.date(year=1900, month=1, day=1))


class ChoosingFilter(models.Model):
    filter_type = models.CharField(max_length=10)
