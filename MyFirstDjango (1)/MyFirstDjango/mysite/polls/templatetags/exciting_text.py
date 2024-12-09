from django import template

register = template.Library()

@register.filter
def exciting_text(value):
    return value + "!!!!!!!!!!!!!!!!!!!!!!"