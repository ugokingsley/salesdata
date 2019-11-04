from django.contrib import admin
from .models import *
from import_export import resources
from import_export.admin import ImportExportModelAdmin
import import_export

'''
@admin.register(SalesData)
class SalesDataAdmin(ImportExportModelAdmin):
    list_display = ('invoice', 'stockcode', 'description', 'quantity', 'invoicedate', 'price', 'customerid')
    #list_filter = ('invoice', 'stockcode', 'description', 'quantity', 'invoicedate', 'price', 'customerid')
'''


class MyModelResource(import_export.resources.ModelResource):

    def after_import_instance(self, instance, new, **kwarg):
        """ For each row in the import file, add the pk to the list """
        self.imported_rows_pks.append(instance.pk)

    def after_import(self, dataset, result, using_transactions, dry_run, **kwargs):
        """  delete all rows not in the import data set.
        Then call the same method in the parent to still sequence the DB """
        self.Meta.model.objects.exclude(pk__in=self.imported_rows_pks).delete()
        import_export.resources.ModelResource.after_import(self, dataset, result, using_transactions, dry_run, **kwargs)


class SalesDataR(MyModelResource):
    imported_rows_pks = []

    class Meta:
        model = SalesData
        import_id_fields = ['invoice', 'stockcode', 'description', 'quantity', 'invoicedate', 'price', 'customerid']


class SalesDataAdmin(ImportExportModelAdmin):
    resource_class = SalesDataR


admin.site.register(SalesData, SalesDataAdmin)