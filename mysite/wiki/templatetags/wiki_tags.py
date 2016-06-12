from django import template
import markdown, re

#wikiWord = re.compile(r"\b([A-Z][a-z]+[A-Z][a-z]+)\b")
wikiWordV2 = re.compile(r"\[\[([A-Za-z0-9_]+)\]\]")

register=template.Library()

@register.filter
def markup(text):
    return markdown.markdown(text)

@register.filter
def wikify(text):
    return wikiWordV2.sub(r'''
    <a href="/wiki/page/\1/">\1</a>
    ''', text)
    