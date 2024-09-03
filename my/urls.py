from django.urls import path
from .views import (HomeView, ContactView, BlogView, 
BlogDetailView, GalleryView, AboutView, ReservationView, StuffView)

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('blog/', BlogView.as_view(), name='blog'),
    path('blog/<int:id>/', BlogDetailView.as_view(), name='blog_detail'),
    path('gallery/', GalleryView.as_view(), name='gallery'),
    path('about/', AboutView.as_view(), name='about'),
    path('reservation/', ReservationView.as_view(), name='reservation'),
    path('stuff/', StuffView.as_view(), name='stuff'),
   
]
