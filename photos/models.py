from django.db import models

class Editor(models.Model):
    name = models.CharField(max_length = 30)
    email = models.EmailField()

    def __str__(self):
        return self.name

class Image(models.Model):
    image =models.ImageField()
    name = models.CharField(max_length = 30)
    description = models.TextField()
    location = models.CharField(max_length = 30)
    category = models.CharField(max_length = 30)

class category(models.Model):
    name=models.CharField(max_length = 20)

    def __str__(self):
        return self.name