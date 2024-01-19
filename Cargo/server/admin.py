from django.contrib import admin
from .models import *

admin.site.register(Car)
admin.site.register(Trip)
admin.site.register(Client)
admin.site.register(Request)
admin.site.register(RequestCost)
admin.site.register(RouteDetail)
