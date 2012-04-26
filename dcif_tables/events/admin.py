from dcif_tables.events.models import *
from django.contrib import admin

class TableAdmin(admin.ModelAdmin):

    list_display = ('number',)

admin.site.register(Table, TableAdmin)
