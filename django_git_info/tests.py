import os, datetime, json
from django.core.exceptions import ImproperlyConfigured
from django.test import TestCase, override_settings, RequestFactory

from django_git_info import get_git_info
from django_git_info.views import git_info
from django_git_info.templatetags.django_git_info_tags import get_git_info as get_git_info_tag

class NoConfigTestCase(TestCase):
    def test_get_git_info(self):
        """This should throw exception"""
        self.assertRaises(ImproperlyConfigured, get_git_info) 
        

DIRNAME = os.path.dirname(__file__)

@override_settings(DJANGO_GIT_REPO=os.path.join(DIRNAME, '..'))
class GitInfoTestCase(TestCase):
    def test_get_git_info(self):
        """Test the API method"""
        info = get_git_info() 
        self.assertTrue('hash' in info )
        self.assertTrue(isinstance(info['commiter_date'], datetime.datetime) )
        
    def test_get_git_info_view(self):
        """Test the json view"""
        request = RequestFactory().get('/')
        response = git_info(request)
        
        self.assertEquals(response.status_code, 200)
        json_resp = json.loads(response.content)
        self.assertTrue('hash' in json_resp)
        
    def test_templatetag(self):
        info = get_git_info_tag() 
        self.assertTrue('hash' in info )
        self.assertTrue(isinstance(info['commiter_date'], datetime.datetime) )