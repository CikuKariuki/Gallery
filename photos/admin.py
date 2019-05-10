from django.contrib import admin
from .models import Editor,Image,Category,Location
class ImageAdmin(admin.ModelAdmin):
    filter_horizontal =('category')
    
admin.site.register(Editor)
admin.site.register(Category)
admin.site.register(Image)
admin.site.register(Location)

