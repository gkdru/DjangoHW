from django.contrib import admin
from .models import Parent, Child, IceCream, IceCreamKiosk


admin.site.register(Parent)
admin.site.register(Child)
admin.site.register(IceCream)
admin.site.register(IceCreamKiosk)
