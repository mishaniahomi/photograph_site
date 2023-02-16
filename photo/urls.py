from django.urls import path, include
from .views import Index, detail_albom, blog, about



urlpatterns = [
    path('gallery', Index.as_view(), name='index'),
    path('<int:albom_id>', detail_albom, name='albom_view'),
    path('blog', blog, name='blog'),
    path('', about, name='about'),

]