# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand, CommandError

from django_git import get_git_info


class Command(BaseCommand):
    help = 'Gets git info'

    #@transaction.commit_manually
    def handle(self, *args, **options):
        print get_git_info()