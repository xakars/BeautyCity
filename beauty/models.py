from django.db import models
from django.core.validators import RegexValidator
from django.core.validators import MaxValueValidator, MinValueValidator


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
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,12}$',
        message='Телефонный номер должен быть в формате: "+79999999999".\
            Допускается до 12 цифр.'
    )
    phone = models.CharField(
        validators=[phone_regex],
        verbose_name='Телефон',
        max_length=12
    )

    class Meta:
        verbose_name = ('Клиент')
        verbose_name_plural = ('Клиенты')

    def __str__(self):
        return self.fullname


class Master(models.Model):
    fullname = models.CharField(verbose_name='Имя', max_length=30)
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,12}$',
        message='Телефонный номер должен быть в формате: "+79999999999".\
            Допускается до 12 цифр.'
        )
    phone = models.CharField(
        validators=[phone_regex]
        verbose_name='Телефон'
        max_length=12
    )
    speciality = models.CharField(verbose_name='Специальность', max_length=150)
    photo = models.ImageField(
        blank=True,
        verbose_name='Фотография'
    )
    start_date = models.DateField(
        'дата начала работы',
        blank=True,
        null=True
    )
    experience = models.DurationField(verbose_name='Стаж', blank=True, null=True)
  
    class Meta:
        verbose_name = _('Мастер')
        verbose_name_plural = _('Мастер')

    def __str__(self):
        return self.fullname
    

class Service(models.Model):
    name = models.CharField(verbose_name='Название услуги', max_length=200)
    price = models.PositiveIntegerField(verbose_name='Цена услуги')
    master = models.ManyToMany(
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
    

class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name="Клиент")
    salon = models.ForeignKey(Salon, on_delete=models.CASCADE, verbose_name="Салон")
    service = models.ForeignKey(Service, on_delete=models.CASCADE, verbose_name="Услуги")
    master = models.ForeignKey(Master, on_delete=models.CASCADE, verbose_name="Мастер")
    date = models.DateField(verbose_name='Дата записи')
    time = models.TimeField(verbose_name='Время записи')

    class Meta:
        verbose_name = _('Заказ')
        verbose_name_plural = _('Заказы')

    def __str__(self):
        return self.name


class Review(models.Model):
    name = models.CharField(verbose_name='Имя', max_length=30)
    master = models.ForeignKey(Master, on_delete=models.CASCADE, verbose_name="Мастер")
    rate = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    review_text = models.TextField(verbose_name="Отзыв", max_length=500)

    class Meta:
        verbose_name = _('Отзыв')
        verbose_name_plural = _('Отзывы')

    def __str__(self):
        return f'{self.name} {self.master} {self.rate}'
