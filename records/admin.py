from .models import *

from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin


# Unregister the provided model admin
admin.site.unregister(User)
# Register out own model admin, based on the default UserAdmin


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        is_superuser = request.user.is_superuser
        disabled_fields = set()  # type: Set[str]
        if not is_superuser:
            disabled_fields |= {
                'username',
                'is_superuser',
            }
        for f in disabled_fields:
            if f in form.base_fields:
                form.base_fields[f].disabled = True
        return form


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
