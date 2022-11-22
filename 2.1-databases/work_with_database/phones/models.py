from django.db import models
from django.urls import reverse
from django.utils.text import slugify

class Phone(models.Model):
    name = models.CharField(max_length = 150, null = False, unique = True)
    image = models.CharField(max_length = 254)
    price = models.IntegerField()
    release_date = models.DateField(null = False)
    lte_exists = models.BooleanField()
    slug = models.SlugField(max_length = 254)
    
    # def get_absolute_url(self):
    #   return reverse ('catalog', kwargs = {'slug': slugify (self.name)})
        
    # TODO: Добавьте требуемые поля
    # pass
