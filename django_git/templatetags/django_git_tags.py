from django import template
from django.template.defaultfilters import stringfilter

import django_git.gitint


register = template.Library()


@register.assignment_tag
def get_git_info():
    return django_git.gitint.get_git_info()