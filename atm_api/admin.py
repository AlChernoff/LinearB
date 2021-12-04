from django.contrib import admin
import requests
# Register your models here.

class MyCurrencyAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        if obj.status == 'approved':
            #Make Api Call
            requests.post("", params={"name":obj.name})
        super().save_model(request, obj, form, change)