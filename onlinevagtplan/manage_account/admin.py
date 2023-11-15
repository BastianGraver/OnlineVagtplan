from django.contrib import admin

from .models import Users, Movies, Shifts

# Register your models here.
admin.site.register(Users)
admin.site.register(Movies)
admin.site.register(Shifts)