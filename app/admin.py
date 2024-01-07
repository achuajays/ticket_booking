from django.contrib import admin
from .models import Movie , Screening , Theater , Ticket
# Register your models here.


admin.site.register(Movie)

admin.site.register(Screening)


admin.site.register(Theater)


admin.site.register(Ticket)