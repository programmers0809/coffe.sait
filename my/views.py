from django.views import View
from django.shortcuts import render

class HomeView(View):
    def get(self, request):
         return render(request, 'coffe/home.html')

class ContactView(View):
    def get(self, request):
        return render(request, 'contact.html')

class BlogView(View):
    def get(self, request):
        return render(request, 'blog.html')

class BlogDetailView(View):
    def get(self, request, id):
        return render(request, 'blog_detail.html', {'id': id})

class GalleryView(View):
    def get(self, request):
        return render(request, 'gallery.html')

class AboutView(View):
    def get(self, request):
        return render(request, 'about.html')

class ReservationView(View):
    def get(self, request):
        return render(request, 'reservation.html')

class StuffView(View):
    def get(self, request):
        return render(request, 'stuff.html')

class MenuView(View):
    def get(self, request, id):
        # ID bo'yicha menyuni olish va render qilish
        return render(request, 'menu.html', {'id': id})

   
