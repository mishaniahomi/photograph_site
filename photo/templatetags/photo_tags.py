from django import template

from photo.models import Photo, Blog

register = template.Library()
@register.simple_tag()
def get_no_alboms_photo():
    return Photo.objects.filter(albom_id=None)

@register.simple_tag()
def get_blog():
    return Blog.objects.all()
