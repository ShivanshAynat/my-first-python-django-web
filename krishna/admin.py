from django.contrib import admin

from .models import Hotels,Rooms,Reservation,Contact
# Register your models here.
admin.site.register(Hotels)
admin.site.register(Rooms)
admin.site.register(Contact)
