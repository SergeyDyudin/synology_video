from django.contrib import admin

from .models import *


class RecordsAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        "slug": ("title", )
    }


admin.site.register(Records, RecordsAdmin)
