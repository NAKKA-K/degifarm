from django import template
register = template.Library()

@register.filter(name = 'index')
def index(value, arg):
  if len(value) <= arg:
    return None
  return value[arg]
