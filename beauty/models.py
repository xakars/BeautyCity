from django.db import models
from datetime import datetime
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField


class Salon(models.Model):
    name = models.CharField(verbose_name='Название салона', max_length=150)
    address = models.CharField(verbose_name='Адрес', max_length=255)
    time_work = models.CharField(verbose_name='Режим работы', max_length=100)
    photo = models.ImageField(
        blank=True,
        verbose_name='Фотография'
    )

    class Meta:
        verbose_name = _('Салон красоты')
        verbose_name_plural = _('Салоны красоты')

    def __str__(self):
        return self.name


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
    phone = PhoneNumberField(
        'Номер клиента',
        blank=True,
        max_length=20,
    )
    speciality = models.CharField(verbose_name='Специальность', max_length=150)
    photo = models.ImageField(
        blank=True,
        verbose_name='Фотография'
    )
    start_date = models.DateField(
        verbose_name='Дата начала работы',
        blank=True,
        null=True
    )
    experience = models.DurationField(
        verbose_name='Стаж',
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = _('Мастер')
        verbose_name_plural = _('Мастера')

    def __str__(self):
        return self.fullname

    def get_experience(self):
        self.experience = datetime.now().date() - \
            (self.start_date if self.start_date else datetime.now().date())
        return self.experience


class Service(models.Model):
    name = models.CharField(verbose_name='Название услуги', max_length=200)
    price = models.PositiveIntegerField(verbose_name='Цена услуги')
    masters = models.ManyToManyField(
        Master,
        related_name='services',
        verbose_name='Мастера'
    )
    photo = models.ImageField(
        blank=True,
        verbose_name='Фотография'
    )

    class Meta:
        verbose_name = _('Услуга')
        verbose_name_plural = _('Услуги')

    def __str__(self):
        return self.name


class Schedule(models.Model):
    STATUSES = [
        ('1', 'Свободно'),
        ('2', 'Занято')
    ]
    date = models.DateField('Дата записи')
    time = models.TimeField('Время записи')
    status = models.CharField(
        'статус',
        max_length=10,
        choices=STATUSES,
        default='available'
    )
    master = models.ForeignKey(
        Master,
        on_delete=models.CASCADE,
        related_name='schedule',
        verbose_name='мастер',
        null=True
    )

    class Meta:
        verbose_name = _('расписание')
        verbose_name_plural = _('расписания')

    def __str__(self):
        return f'{self.date} {self.time} {self.master} {self.status}'


class Order(models.Model):
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
    datetime = models.ForeignKey(
        Schedule,
        on_delete=models.CASCADE,
        verbose_name='Время записи'
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
