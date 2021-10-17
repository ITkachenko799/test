from django.db import models


class Restaurant(models.Model):
    name = models.CharField(max_length=64, blank=False, verbose_name="Ресторан")
    special = models.CharField(max_length=64, blank=False, verbose_name="Специализация")
    address = models.CharField(max_length=64, blank=False, verbose_name="Адрес")
    phone_number = models.CharField(max_length=64, blank=False, unique=True, verbose_name="Номер телефона")

    class Meta:
        verbose_name = 'Ресторан'
        verbose_name_plural = 'Рестораны'

    def __str__(self):
        return f"{self.name} {self.special} {self.address} {self.phone_number}"

