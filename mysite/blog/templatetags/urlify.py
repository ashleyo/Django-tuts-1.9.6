from urllib.parse import quote
from django import template
import markdown

register = template.Library()

@register.filter
def urlify(value):
    return quote(value)

@register.filter
def markup(text):
    return markdown.markdown(text)
