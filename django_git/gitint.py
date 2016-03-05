from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
import git
import json

def get_git_info():
    try:
        r = git.Repo(settings.DJANGO_GIT_REPO)
        git_resp = r.git.log(pretty='{"hash":"%H", "subject":"%s", "commiter_date":"%cd"}', n=1, date='format:%Y-%m-%d:%H:%M%S')
        return json.loads(git_resp)
    except AttributeError:
        raise ImproperlyConfigured("Please add a 'DJANGO_GIT_REPO' setting with the base of your git project to your settings.py")