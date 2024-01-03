from .views import index, aboutus, notification, gallery, publication, media
from django.urls import path, include

urlpatterns = [
    path('', index, name="home"), 
    path('about/', aboutus, name="about"), 
    path('notification/', notification, name="notification"), 
    path('media/', media, name="media"), 
    path('gallery/', gallery, name="gallery"), 
    path('publication/', publication, name="publication"), 
]
