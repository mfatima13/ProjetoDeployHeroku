from django.template import Library

register = Library()

@register.filter
def arredonda(value, casas):
    return round(value, casas)