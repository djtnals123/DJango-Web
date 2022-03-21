from django import template
from django.http import request

register = template.Library()


@register.filter
def first_error(value):
    return list(value)[0][1][0]


@register.filter
def format_datetime(value, fmt='%Y-%m-%d'):
    return value.strftime(fmt)


@register.filter
def roles(user):
    roles_str = ''
    if user.is_staff:
        roles_str += '관리자 '
    for group in user.groups.all():
        roles_str += str(group) + ' '
    return roles_str


@register.filter
def hospital(user):
    if user.hospital == 'S':
        return '서울대병원'
    elif user.hospital == 'K':
        return '고려대병원'


@register.filter
def has_group(user, group):
    for g in user.groups.all():
        if str(g) == group:
            return True
    return False
