from django.core.management import BaseCommand
from catalog.models import Product, Category


class Command(BaseCommand):
    def handle(self, *args, **options):
        category_list = [
            {'category_name': 'Овощи', 'category_description': 'Их можно есть'},
            {'category_name': 'Фрукты', 'category_description': 'Их тоже можно есть'},
            {'category_name': 'Соки', 'category_description': 'Их пьют'},
            {'category_name': 'Кофе', 'category_description': 'Он заваривается'},
            {'category_name': 'Мясо', 'category_description': 'Только свежее'},
            {'category_name': 'Рыба', 'category_description': 'Когда то плавала'},
        ]

        # for product in category_list:
        #     Category.objects.create(**product)

        category_for_create = []
        for category in category_list:
            category_for_create.append(Category(**category))
        Category.objects.bulk_create(category_for_create)