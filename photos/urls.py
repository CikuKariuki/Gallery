from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    url(r'^$',views.photos_of_day,name='photosToday'),
    url(r'^archives/(\d{4}-\d{2}-\d{2})/$',views.past_photos,name='pastPhotos')
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)