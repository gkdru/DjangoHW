
from django import template
custom = template.Library()

@custom.filter
def custom_add(value1, value2)-> int:
    return f'{int(value1)}+{int(value2)}'
