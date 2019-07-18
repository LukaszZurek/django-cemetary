from django.contrib import admin
from .models import Place, DeadPerson, Cemetary

admin.site.register(DeadPerson)
admin.site.register(Cemetary)
admin.site.register(Place)
# Register your models here.
