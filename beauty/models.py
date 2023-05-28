from django.db import models
from datetime import datetime
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField


class Category(models.Model):
    name = models.CharField(
        'Категория',
        max_length=25
    )

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Client(models.Model):
    fullname = models.CharField(verbose_name='Имя', max_length=255)
    phone = PhoneNumberField(
        'Номер клиента',
        blank=True,
        max_length=20,
    )

    class Meta:
        verbose_name = _('Клиент')
        verbose_name_plural = _('Клиенты')

    def __str__(self):
        return self.fullname


class Master(models.Model):
    fullname = models.CharField(verbose_name='Имя', max_length=30)

    speciality = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        default=None,
        verbose_name='Специальность',
        null=True,
        blank=True,
    )

    photo = models.ImageField(
        blank=True,
        verbose_name='Фотография'
    )

    class Meta:
        verbose_name = _('Мастер')
        verbose_name_plural = _('Мастера')

    def __str__(self):
        return self.fullname



class Salon(models.Model):
    name = models.CharField(verbose_name='Название салона', max_length=150)
    address = models.CharField(verbose_name='Адрес', max_length=255)
    photo = models.ImageField(
        blank=True,
        verbose_name='Фотография'
    )
    master = models.ManyToManyField(
        'Master',
        through='DayOfWork',
        through_fields=('salons', 'master')
    )

    class Meta:
        verbose_name = _('Салон красоты')
        verbose_name_plural = _('Салоны красоты')

    def __str__(self):
        return self.name


class Service(models.Model):
    name = models.CharField(verbose_name='Название услуги', max_length=200)
    price = models.PositiveIntegerField(verbose_name='Цена услуги')
    photo = models.ImageField(
        blank=True,
        verbose_name='Фотография'
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='services',
        default=None,
        verbose_name='Категории',
        null = True,
        blank = True,
    )

    class Meta:
        verbose_name = _('Услуга')
        verbose_name_plural = _('Услуги')

    def __str__(self):
        return self.name


class DayOfWork(models.Model):
    MONDAY = 'Mo'
    TUESDAY = 'Tu'
    WEDNESDAY = 'We'
    THURSDAY = 'Td'
    FRIDAY = 'Fr'
    SATURDAY = 'Sa'
    SUNDAY = 'Su'

    DAYS_OF_WEEK = [
        (MONDAY, 'Пн'),
        (TUESDAY, 'Вт'),
        (WEDNESDAY, 'Ср'),
        (THURSDAY, 'Чт'),
        (FRIDAY, 'Пт'),
        (SATURDAY, 'Сб'),
        (SUNDAY, 'Вс')
    ]

    day_of_week = models.CharField(
        max_length=20,
        verbose_name='Рабочие дни',
        choices=DAYS_OF_WEEK,
        blank=True
    )

    ready = models.BooleanField(
        default=False
    )

    master = models.ForeignKey(
        Master,
        on_delete=models.CASCADE,
        related_name='day_of_works',
        verbose_name='Мастер'
    )

    salons = models.ForeignKey(
        Salon,
        on_delete=models.CASCADE,
        related_name='day_of_works'
    )


class Order(models.Model):
    MORNING_1 = '9:00'
    MORNING_2 = '10:00'
    MORNING_3 = '11:00'
    AFTERNOON_1 = '12:00'
    AFTERNOON_2 = '13:00'
    AFTERNOON_3 = '14:00'
    DAY_1 = '15:00'
    DAY_2 = '16:00'
    DAY_3 = '17:00'
    EVENING_1 = '18:00'
    EVENING_2 = '19:00'
    EVENING_3 = '20:00'
    day_times = {
        MORNING_1, MORNING_2, MORNING_2, MORNING_3, AFTERNOON_1, AFTERNOON_2,
        AFTERNOON_3, DAY_1, DAY_2, DAY_3, EVENING_1, EVENING_2, EVENING_3
    }
    WORK_HOURS = [
        (MORNING_1, MORNING_1),
        (MORNING_2, MORNING_2),
        (MORNING_3, MORNING_3),
        (AFTERNOON_1, AFTERNOON_1),
        (AFTERNOON_2, AFTERNOON_2),
        (AFTERNOON_3, AFTERNOON_3),
        (DAY_1, DAY_1),
        (DAY_2, DAY_2),
        (DAY_3, DAY_3),
        (EVENING_1, EVENING_1),
        (EVENING_2, EVENING_2),
        (EVENING_3, EVENING_3),
    ]

    client = models.ForeignKey(
        Client,
        on_delete=models.CASCADE,
        verbose_name='Клиент'
    )

    salon = models.ForeignKey(
        Salon,
        on_delete=models.CASCADE,
        verbose_name='Салон'
    )
    service = models.ForeignKey(
        Service,
        on_delete=models.CASCADE,
        verbose_name='Услуги'
    )
    master = models.ForeignKey(
        Master,
        on_delete=models.CASCADE,
        verbose_name='Мастер'
    )
    appointment_hour = models.CharField(
        max_length=15,
        verbose_name='Время записи',
        choices=WORK_HOURS,
        blank=True
    )
    client_name = models.CharField('имя клиента', max_length=100, null=True, blank=True)
    date = models.DateField(
        'Дата',
        null=True
    )

    class Meta:
        verbose_name = _('Заказ')
        verbose_name_plural = _('Заказы')

    def __str__(self):
        return str(self.id)


class Review(models.Model):
    name = models.CharField(verbose_name='Имя', max_length=30)
    master = models.ForeignKey(
        Master,
        on_delete=models.CASCADE,
        verbose_name='Mастер'
    )
    RATE_CHOICES = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
    )
    rate = models.PositiveSmallIntegerField(
        verbose_name="Оцените от 1 до 5",
        choices=RATE_CHOICES)
    review_text = models.TextField(verbose_name="Отзыв", max_length=500)

    class Meta:
        verbose_name = _('Отзыв')
        verbose_name_plural = _('Отзывы')

    def __str__(self):
        return f'{self.name} {self.master} {self.rate}'
