from django.contrib import admin
from .models import CustomerHouseHold,Transaction,MetreReading
# Register your models here.


# @admin.register(MetreReading)
class MetreReadingAdmin(admin.ModelAdmin):
    list_display = ('owner','voltage','current')
    # list_filter = ('',)
    # raw_id_fields = ('',)
    # readonly_fields = ('',)
    # search_fields = ('',)
    # date_hierarchy = ''
    # ordering = ('',)

class TransactionAdmin(admin.ModelAdmin):
    list_display = ('buyer', 'date', 'units')
    
admin.site.register(CustomerHouseHold)
admin.site.register(Transaction)
admin.site.register(MetreReading)