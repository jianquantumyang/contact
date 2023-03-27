
from django import template
from django.template.defaultfilters import stringfilter

import markdown as md

register = template.Library()

# @register.filter()
# def convert_markdown(value):
#     return md.markdown(value)

@register.filter()
@stringfilter
def markdown(value):
    return md.markdown(value, extensions=['markdown.extensions.fenced_code'])