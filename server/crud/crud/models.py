from django.db import models


# создаем таблицу в базе данных
class DetailsModel(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    age = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

    # выводим в базу данных по имени, если оно есть
    def __str__(self):
        return self.name or ''