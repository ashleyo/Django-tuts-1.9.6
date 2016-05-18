from django import template
import markdown, re

wikiWord = re.compile(r"\b([A-Z][a-z]+[A-Z][a-z]+)\b")

register=template.Library()

@register.filter
def markup(text):
    return markdown.markdown(text)

@register.filter
def wikify(text):
    return wikiWord.sub(r'''
    <a href="/wiki/\1/">\1</a>
    ''', text)
    