from django import template
from urllib.parse import urlencode

register = template.Library()


@register.simple_tag
def query_string(*_, **kwargs):
    safe_args = {k: v for k, v in kwargs.items() if (v is not None) and (v is not '')}
    if safe_args:
        return '?{}'.format(urlencode(safe_args))
    return ''


@register.simple_tag
def get_proper_elided_page_range(page_obj, on_each_side=3, on_ends=2):
    return page_obj.paginator.get_elided_page_range(number=page_obj.number, on_each_side=on_each_side, on_ends=on_ends)

