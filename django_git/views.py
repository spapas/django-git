from django.http import HttpResponse
from django.shortcuts import render
import json 
from gitint import get_git_info

def git_info(request):
    data = get_git_info()
    
    return HttpResponse(json.dumps(data), content_type='application/json')