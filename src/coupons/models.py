from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Coupon(models.Model):
    code = models.CharField(max_length=60, unique=True, verbose_name='Код купона')
    valid_from = models.DateTimeField(verbose_name='начало действия купона')
    valid_to = models.DateTimeField(verbose_name='окончание действия купона')
    discount = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], verbose_name='Применяемая ставка дисконта')
    active = models.BooleanField()

    def __str__(self):
        return self.code
