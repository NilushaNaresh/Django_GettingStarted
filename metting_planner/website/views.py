from datetime import datetime

from django.shortcuts import render
from django.http import HttpResponse
from meetings.models import Meeting


# Create your views here.
def welcome(request):
    #return render(request,"website/welcome.html", {"message":'This message is passed to the template',"name":'Nilusha Naresh',"number_of_meetings":Meeting.objects.count()})
    return render(request,"website/welcome.html", {"message": 'This message is passed to the template',"name": 'Nilusha Naresh',"meetings": Meeting.objects.all()})


def date(request):
    return HttpResponse("The serving date is: " + str(datetime.now()))

def info_myself(request):
    return HttpResponse("Name : Nilusha")