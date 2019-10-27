from django.contrib import admin
from .models import *
from import_export import resources
from import_export.admin import ImportExportModelAdmin


@admin.register(SalesData)
class SalesDataAdmin(ImportExportModelAdmin):
    list_display = ('invoice', 'stockcode', 'description', 'quantity', 'invoicedate', 'price', 'customerid')
    #list_filter = ('invoice', 'stockcode', 'description', 'quantity', 'invoicedate', 'price', 'customerid')





