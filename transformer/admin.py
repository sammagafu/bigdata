from django.contrib import admin
from .models import Transformer, TransformerReading
# Register your models here.
admin.site.register(Transformer)
admin.site.register(TransformerReading)