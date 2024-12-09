import datetime
from django import template

register = template.Library()

@register.simple_tag
def time_test():
    return datetime.datetime.now()