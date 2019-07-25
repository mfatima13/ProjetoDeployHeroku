from django.template import Library
from datetime import datetime

register = Library()

@register.simple_tag(takes_context=True)
def current_time(context, format_string):
    return datetime.now().strftime(format_string)

@register.simple_tag()
def footer_mensage():
    return 'Desenvolvimento web com Django 2.2.2'

# TODO: IMPLEMENTAR UMA PAGINAÇÃO NA LISTA DE CLIENTES, AQUI OU EM FILTERS!
#não fazer regras de negocio, e nem acessar models nessa parte, aqui e o T do MVT