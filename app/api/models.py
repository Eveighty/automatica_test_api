from django.db import models

# Create your models here.
class Employee(models.Model):
    """Работник"""
    class Meta:
        verbose_name = 'Работник'
        verbose_name_plural = 'Работники'

    name = models.CharField(max_length=150, verbose_name='Имя')
    # для упрощения телефон строкой
    phone = models.CharField(max_length=50, verbose_name='# Телефона')

    def __str__(self) -> str:
        return self.name


class RetailPoint(models.Model):
    """Торговая точка"""
    class Meta:
        verbose_name = 'Торговая точка'
        verbose_name_plural = 'Торговые точки'

    title = models.CharField(max_length=200, verbose_name='Название')
    employee = models.ForeignKey(Employee, null=True, on_delete=models.SET_NULL, verbose_name='Работник')

    def __str__(self) -> str:
        return self.title


class Visit(models.Model):
    """Посещение"""
    class Meta:
        verbose_name = 'Посещение'
        verbose_name_plural = 'Посещения'

    retail_point = models.ForeignKey(RetailPoint, on_delete=models.CASCADE, verbose_name='Торговая точка')
    visit_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата')
    # для упрощения координаты строкой, например: широта; долгота
    coordinates = models.CharField(max_length=40,  blank=True, null=True, verbose_name='Координаты')

