from django import template

register = template.Library()

@register.simple_tag
def range_tag(start, end):
    return range(start, end)