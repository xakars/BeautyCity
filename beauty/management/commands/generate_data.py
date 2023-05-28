from django.core.management.base import BaseCommand, CommandError
from beauty.models import Salon, Master, Service, Category
from django.conf import settings
from django.core.files import File
import random



class Command(BaseCommand):
    def handle(self, *args, **options):
        saloons = [
            {'name': 'BeautyCity Пушкинская', 'address': 'ул. Пушкинская, д. 78А', 'photo': 'salon1.svg', 'time_work': '10:00-21:00'},
            {'name': 'BeautyCity Ленина', 'address': 'ул. Ленина, д. 211', 'photo': 'salon2.svg', 'time_work': '10:00-21:00'},
            {'name': 'BeautyCity Красная', 'address': 'ул. Красная, д. 10', 'photo': 'salon3.svg', 'time_work': '10:00-21:00'},
        ]

        for saloon in saloons:
            new_saloon, created = Salon.objects.get_or_create(
                name=saloon['name'],
                address=saloon['address'],
            )
            if created:
                local_file = open(f'{settings.BASE_DIR}/beauty/static/img/salons/{saloon["photo"]}', "rb")
                djangofile = File(local_file)
                new_saloon.photo.save(f'beauty/{saloon["photo"]}', djangofile)
                local_file.close()

        masters = [

            {'fullname': 'Елизавета Лапина', 'speciality': 'Мастер маникюра', 'phone': '+77773452323' ,'photo': 'master1.svg', 'start_date': '2023-03-25'},
            {'fullname': 'Анастасия Сергеева', 'speciality': 'Парикмахер', 'phone': '+77773457723' ,'photo': 'master2.svg', 'start_date': '2020-03-25'},
            {'fullname': 'Ева Колесова', 'speciality': 'Визажист', 'phone': '+77773454423' ,'photo': 'master3.svg', 'start_date': '2014-03-25'},
            {'fullname': 'Мария Суворова', 'speciality': 'Стилист', 'phone': '+77773992323' ,'photo': 'master4.svg', 'start_date': '2011-03-25'},

        ]

        categories = [{'name':'Парикмахерские услуги'}, {'name': 'Макияж'}]

        for category in categories:
            new_category, created = Category.objects.get_or_create(
                name=category['name'],
            )

        categories = Category.objects.all()
        for master in masters:
            new_master, created = Master.objects.get_or_create(
                fullname=master['fullname'],
            )
            if categories:
                random_category = random.choice(categories)
                new_master.speciality = random_category
            new_master.save()
            if created:
                local_file = open(f'{settings.BASE_DIR}/beauty/static/img/masters/{master["photo"]}', "rb")
                djangofile = File(local_file)
                new_master.photo.save(f'{master["photo"]}', djangofile)
                local_file.close()

        services = [

            {'name': 'Дневной макияж', 'price': 1400, 'masters': '', 'photo': 'service1.svg'},
            {'name': 'Маникюр. Классический. Гель', 'price': 2000, 'masters': '', 'photo': 'service2.svg'},
            {'name': 'Укладка волос', 'price': 1500, 'masters': '', 'photo': 'service3.svg'},
        ]


        for service in services:
            new_service, created = Service.objects.get_or_create(
                name=service['name'],
                price=service['price'],
            )

            if categories:
                random_category = random.choice(categories)
                new_service.speciality = random_category
            new_service.save()

            if created:
                local_file = open(f'{settings.BASE_DIR}/beauty/static/img/services/{service["photo"]}', "rb")
                djangofile = File(local_file)
                new_service.photo.save(f'{service["photo"]}', djangofile)
                local_file.close()
