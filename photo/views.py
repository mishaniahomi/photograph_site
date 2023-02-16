from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.views.generic.list import ListView
from django.views.generic import DetailView
from .models import Albom, Photo, AboutMe, Blog


class Index(ListView):
    context_object_name = 'alboms'
    template_name = 'photo/detail_albom.html'

    def get_queryset(self):
        return Albom.objects.all()


def detail_albom(request, albom_id):
    albom = get_object_or_404(Albom, pk=albom_id)
    photos = Photo.objects.filter(albom_id=albom_id)
    alboms = Albom.objects.all()
    context = {'albom': albom, 'photos': photos, 'alboms': alboms}
    return render(request, 'photo/detail_albom.html', context)


def blog(request):
    blogs = Blog.objects.all()
    return render(request, 'photo/blog.html', {'blogs': blogs,'selector':1})


def about(request):
    about_data = AboutMe.objects.first()
    return render(request, 'photo/about.html', {'about_data': about_data,'selector':2})
