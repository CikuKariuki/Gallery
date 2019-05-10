from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
import datetime as dt 
from .models import Image

def welcome(request):
    return render(request,'welcome.html')

def photos_of_day(request):
    date = dt.date.today()
    photos = Image.objects.all()
    return render(request,'all-photos/today_photos.html',{"date": date,"photos":photos,})

def past_photos(request,past_date):
    try:
        #converts data from the string url
        date = dt.datetime.strptime(past_date,'%Y-%m-%d').date()
    except ValueError:
        raise Http404()
        assert False

    if date == dt.date.today():
        return redirect(photos_of_day)
    else:
        return redirect(past_photos)

    return render(request,'all-photos/past_photos.html',{"date": date})

def search_results(request):
    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_images = Image.search_by_category(search_term)
        message = f"{search_term}"
        return render(request,'all-photos/search.html',{"message":message,"images":searched_images})
    else:
        message = "Please check for spelling or search another term"
        return render(request,'all-photos/search.html',{"message":message,"images":searched_images,})