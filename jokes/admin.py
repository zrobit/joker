from django.contrib import admin

from pics.models import Category, Tag, Joke
# Register your models here.
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Joke)
