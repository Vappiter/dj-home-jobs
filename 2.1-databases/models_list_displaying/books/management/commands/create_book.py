import random

from django.core.management.base import BaseCommand
from books.models import Book

class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
       
        for i in range (1,20):
            books = Book(name = random.choice(['Name #1', 'Name #2', 'Name #3', 'Name #4', 'Name #5']), 
                         author = random.choice(['Author #1', 'Author #2', 'Author #3', 'Author #4']), 
                         pub_date = random.choice(['2022-11-01', '2022-11-02', '2022-11-03', '2022-11-05', '2022-11-07','2022-11-11','2022-11-12']) 
                        )
            books.save()
 