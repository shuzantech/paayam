from django.shortcuts import render
from .models import Gallery, Notifications, Publications, Media

# Create your views here.

def index(request):
    return render(request, "uploads/index.html")


def aboutus(request):
    return render(request, "uploads/about.html")


def notification(request):
    notify = Notifications.objects.all()
    context = {'notifications': notify}
    return render(request, "uploads/notification.html", context)

def media(request):
    media = Media.objects.all()
    
    return render(request, "uploads/media.html", {"media": media})


def gallery(request):
    gallery = Gallery.objects.all()
    context = {'gallery': gallery}
    return render(request, "uploads/gallery.html", context)
 

def publication(request):
    docs = Publications.objects.all()
    context = {'publication' : docs}
    return render(request, "uploads/publication.html", context)