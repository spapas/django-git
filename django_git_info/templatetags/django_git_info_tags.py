from django import template
from django.template.defaultfilters import stringfilter

import django_git_info


register = template.Library()


@register.assignment_tag
def get_git_info():
    return django_git_info.get_git_info()