import logging
from django import template

register = template.Library()

logger = logging.getLogger(__name__)


@register.simple_tag(takes_context=True)
def bankrate_tracking(context):
    try:
        request = context['request']
        return request.utm_tokens.source
    except:
        return "none"
