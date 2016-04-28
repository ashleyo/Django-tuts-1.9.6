from django import template
import markdown

register=template.Library()

@register.filter
def markup(text):
    return markdown.markdown(text)
