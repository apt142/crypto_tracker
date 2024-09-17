from django.contrib import admin

from .models import CurrencySpecificDatem
from .models import RawCurrencySnapshot

admin.site.register(RawCurrencySnapshot, admin.ModelAdmin)
admin.site.register(CurrencySpecificDatem, admin.ModelAdmin)
