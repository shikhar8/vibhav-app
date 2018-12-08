from django.contrib import admin
from .models import signupp
from .models import eventlist
from .models import eventpass
# Register your models here.
admin.site.register(signupp)
admin.site.register(eventlist)
admin.site.register(eventpass)