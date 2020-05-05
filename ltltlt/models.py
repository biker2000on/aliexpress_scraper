from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Item(models.Model):
    item_number = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item_name = models.CharField(max_length=200)
    created_date = models.DateTimeField()
    def __str__(self):
        return self.item_name
    
class Price(models.Model):
    price = models.DecimalField(decimal_places=2, max_digits=10)
    datetime = models.DateTimeField('Date Scraped')
    currency = models.CharField(max_length=3)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.price)

