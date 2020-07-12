from django.contrib import admin

# Register your models here.
from import_export.admin import ImportExportModelAdmin
from .models import Stock
@admin.register(Stock)
class Stock(ImportExportModelAdmin):
    # list_display=("Stock","Script","Name","Price","High","Low")
    pass
