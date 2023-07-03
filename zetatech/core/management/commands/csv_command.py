from django.core.management.base import BaseCommand
from django.core.management import CommandError
import csv
from catalog.models import Product

class Command(BaseCommand):
    help = 'Загрузка из файла cvs в БД'

    def add_arguments(self, parser):
        parser.add_argument('text_csv', 
                            type=str, 
                            help='Название файла csv')

    def handle(self, *args, **options):
        text_csv = options['text_csv'] # название файла
        with open(text_csv, newline='') as csvfile:
            text = csv.DictReader(csvfile, 
                              delimiter=',',
                              quotechar='"'
                              )

            for row in text:
                context = {
                    'title': row.get('title'),
                    'slug': row.get('slug'),
                    'description': row.get('description'),
                    'h1': row.get('h1'),
                    'mini_content': row.get('mini_content'),
                    'price': row.get('price'),
                    'pup_date': row.get('pup_date'),
                    'h2': row.get('h2'),
                    'content': row.get('content'),
                    'catalog': None,
                    'tag': None,
                    'upload': row.get('upload'),
                }
                for key in context:
                    if context[key] == '':
                        context[key] = None
               
                data = Product(**context)
                data.save()

        

 
