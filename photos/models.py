from django.db import models
import datetime as dt 

class Category(models.Model):
    category =models.CharField(max_length = 20)

    def __str__(self):
        return self.category

class Location(models.Model):
    location =models.CharField(max_length = 50)

    def __str__(self):
        return self.location



class Editor(models.Model):
    name = models.CharField(max_length = 30)
    email = models.EmailField()

    def save_editor(self):
        self.save()

    def __str__(self):
        return self.name



class Image(models.Model):
    image =models.ImageField(upload_to = 'photos/')
    caption = models.CharField(max_length = 100)
    description = models.TextField()
    location = models.ForeignKey(Location)
    editor = models.ForeignKey(Editor)
    category = models.ForeignKey(Category)
    pub_date =models.DateTimeField(auto_now_add = True)

    @classmethod
    def search_by_category(cls,search_term):
        photos = cls.objects.filter(category__category__icontains = search_term)

        return photos

    def delete_image(self):
       self.delete()

    def save_image(self):
        self.save()