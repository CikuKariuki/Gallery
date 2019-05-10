from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.photos_of_day,name='photosToday'),
    url(r'^archives/(\d{4}-\d{2}-\d{2})/$',views.past_photos,name='pastPhotos')
]
