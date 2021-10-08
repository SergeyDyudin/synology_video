"""Module for custom template tags and filters"""
from django.template import Library


register = Library()


@register.filter(name='prev_val')
def prev_val(value, arg):
    try:
        return value[int(arg) - 1]
    except Exception:
        return None
