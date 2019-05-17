from django.contrib import admin
from produkt.models import *

class SubscriberAdmin (admin.ModelAdmin):
    list_display = ["id", "name", "email"]
    list_filter = ['name',]
    search_fields = ['name',]
    class Meta:
        model = Subscribers
    
admin.site.register(Settings)
admin.site.register(Produkt)
admin.site.register(Subscribers, SubscriberAdmin)
# Register your models here.
