
from django import template
register = template.Library()

@register.filter
def custom_add(value1, value2)-> str:
    return {str(value1)}+{str(value2)}
