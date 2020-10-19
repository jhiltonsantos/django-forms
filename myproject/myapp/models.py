from django.db import models


class Reporter(models.Model):
    name = models.CharField(max_length=70)
    
    def __str__(self):
        return self.name


class Article(models.Model):
    pub_date = models.DateTimeField()
    headline = models.CharField(max_length=200)
    content = models.TextField()
    reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.headline


class Client(models.Model):
    name = models.CharField(max_length=70)
    
    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(decimal_places=2, max_digits=9)

    def __str__(self):
        return self.name


class Purchase(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    
    def __str__(self):
        return self.client


class Actor(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=70)
    synopsis = models.CharField(max_length=2000)
    actors = models.ManyToManyField(Actor)
    
    def __str__(self):
        return self.title
