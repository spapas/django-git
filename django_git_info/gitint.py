from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
import datetime
import git
import json

formats = (
    ('hash', '%H'),
    ('abbr_hash', '%h'),
    ('subject', '%s'),
    ('sanitized_subject', '%f'),
    ('body', '%b'),
    ('author_name', '%an'), 
    ('author_email', '%ae'), 
    ('author_date', '%ad'), 
    ('commiter_name', '%cn'),
    ('commiter_email', '%ce'),
    ('commiter_date', '%cd'),
)

def format_formats(f):
    ff = ','.join( ['"{0}":"{1}"'.format(x[0], x[1]) for x in formats])
    return '{' + ff +'}'

formatted_formats = format_formats(formats)

def parse_date(d):
    return datetime.datetime.strptime(d, "%Y-%m-%dT%H:%M:%S")

def get_git_info():
    
    try:
        r = git.Repo(settings.DJANGO_GIT_REPO)
        git_resp = r.git.log(pretty=formatted_formats, n=1, date='format:%Y-%m-%dT%H:%M:%S')
        git_resp = git_resp.replace('\n', '\\n')
        json_resp = json.loads(git_resp)
        json_resp['body'] = json_resp['body'].replace('\\n', '\n')
        json_resp['commiter_date'] = parse_date(json_resp['commiter_date'])
        json_resp['author_date'] = parse_date(json_resp['author_date'])
        
        return json_resp
    except AttributeError:
        raise ImproperlyConfigured("Please add a 'DJANGO_GIT_REPO' setting with the base of your git project to your settings.py")