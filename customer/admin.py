from django.contrib import admin
from .models import CustomerHouseHold,Transaction,MetreReading
# Register your models here.
admin.site.register(CustomerHouseHold)
admin.site.register(Transaction)
admin.site.register(MetreReading)