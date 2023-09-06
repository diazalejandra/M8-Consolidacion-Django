from django.contrib import admin
from tienda.models import Salesorderheader
# Register your models here.


class SalesorderheaderAdmin(admin.ModelAdmin):
    list_display = ("salesorderid", "shipdate", "status")


admin.site.register(Salesorderheader, SalesorderheaderAdmin)