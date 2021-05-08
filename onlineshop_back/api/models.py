from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
    
    def __str__(self):
        return '{}'.format(self.name)
    
class Product(models.Model):
    category = models.ForeignKey(Category, related_name = 'products', on_delete = models.CASCADE)
    name = models.CharField(max_length=100)
    image = models.CharField(max_length=255, default='https://images.unsplash.com/photo-1460353581641-37baddab0fa2?ixid=MnwxMjA3fDB8MHxzZWFyY2h8NHx8c2hvZXN8ZW58MHx8MHx8&ixlib=rb-1.2.1&w=1000&q=80')
    description = models.TextField(blank=True)
    price = models.PositiveIntegerField(default=0)

    def __str__(self):
        return '{}'.format(self.name)

class OrderManager(models.Manager):
    def for_user(self, user):
        return self.filter(user=user)

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    product_name = models.CharField(max_length=100, default="TIE-DYE CROP TOP")
    count = models.IntegerField(default=1)
    objects = OrderManager()

    def __str__(self):
        return '{}: {}'.format(self.product_name, self.count)
    
class Review(models.Model):
    text = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return '{}'.format(self.author)

