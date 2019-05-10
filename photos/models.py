from django.db import models

class Editor(models.Model):
    name = models.CharField(max_length = 30)
    email = models.EmailField()

    def save_editor(self):
        self.save()

    def __str__(self):
        return self.name

class Image(models.Model):
    image =models.ImageField()
    name = models.CharField(max_length = 100)
    description = models.TextField()
    location = models.CharField(max_length=100,blank=True)
    # editor = models.ForeignKey(Editor)
    category = models.CharField(max_length = 10)
    # pub_date =models.DateTimeField(auto_now_add = True)

class Category(models.Model):
    name=models.CharField(max_length = 20)

    def __str__(self):
        return self.name

class Location(models.Model):
    name=models.CharField(max_length = 50)

    def __str__(self):
        return self.name