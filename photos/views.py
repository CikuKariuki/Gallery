from django.shortcuts import render
from django.http import HttpResponse,Http404
import datetime as dt 

def welcome(request):
    return HttpResponse('Welcome to my gallery!')

def photos_of_day(request):
    date = dt.date.today()
    day = convert_dates(date)
    html = f'''
        <html>
            <body>
                <h1>Today is {day}, the {date.day}th day of {date.month}th month of the year {date.year}</h1>
            </body>
        </html>
            '''
    return HttpResponse(html)

def convert_dates(dates):
    day_number = dt.date.weekday(dates)
    days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
    day = days[day_number]
    return day

def past_photos(request,past_date):
    try:
        #converts data from the string url
        date = dt.datetime.strptime(past_date,'%Y-%m-%d').date()
    except ValueError:
        raise Http404()

    day = convert_dates(date)
    html = f'''
        <html>
            <body>
                <h1>Photos from {day}, the {date.day}th day of {date.month} month of the year {date.year}</h1>
            </body>
        </html>
            '''
    return HttpResponse(html)