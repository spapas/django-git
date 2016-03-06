from django.http import HttpResponse
from django.shortcuts import render
import json 
from django_git_info.gitint import get_git_info
from datetime import datetime

# FROM http://stackoverflow.com/a/22238613
def json_serial(obj):
    """JSON serializer for objects not serializable by default json code"""

    if isinstance(obj, datetime):
        serial = obj.isoformat()
        return serial
    raise TypeError ("Type not serializable")
    

def git_info(request):
    data = get_git_info()
    
    return HttpResponse(json.dumps(data, default=json_serial), content_type='application/json')