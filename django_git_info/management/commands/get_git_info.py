# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand, CommandError

from django_git_info import get_git_info


class Command(BaseCommand):
    help = 'Gets git info'

    #@transaction.commit_manually
    def handle(self, *args, **options):
        info = get_git_info()
        for key in info.keys():
            print '{0}={1}'.format(key, info[key])