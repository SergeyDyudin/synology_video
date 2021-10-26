from django.contrib import admin

from .models import *


class RecordsAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        "slug": ("title", )
    }
    readonly_fields = ['count_views', 'time_create', 'time_update']
    # fields = ['title', 'date', 'slug']
    fieldsets = [
        (None, {'fields': ['title', 'description', 'date', 'file', 'type', 'public', ]}),
        ('Служебная информация', {'fields': ['slug', 'count_views', 'time_create', 'time_update']})
    ]
    list_display = ('title', 'public', 'count_views', 'date')
    list_editable = ('public',)
    list_filter = ['date', 'public']
    search_fields = ['title']
    save_on_top = True
    date_hierarchy = 'date'


admin.site.register(Records, RecordsAdmin)
