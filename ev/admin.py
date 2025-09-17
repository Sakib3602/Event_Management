from django.contrib import admin
from ev.models import Event, Participent, Category
# Register your models here.
admin.site.register(Event)
admin.site.register(Participent)
admin.site.register(Category)