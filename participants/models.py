from django.db import models


class Participant(models.Model):
    full_name = models.CharField(max_length=255, verbose_name="Ф.И.О")
    country = models.CharField(max_length=100, verbose_name="Страна")
    position = models.CharField(max_length=255, verbose_name="Должность")
    workplace = models.CharField(max_length=255, verbose_name="Место работы")
    academic_degree = models.CharField(max_length=255, verbose_name="Научная степень", blank=True, null=True)
    thesis_title = models.CharField(max_length=500, verbose_name="Название тезиса")

    def __str__(self):
        return self.full_name
