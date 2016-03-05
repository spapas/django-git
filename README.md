# django-git

A very simple app to get informatin from the git repository of your project.

Just add a ``DJANGO_GIT_REPO = REPO_DIR`` setting to your settings.py - ``BASE_DIR``
is where your git repository resides - usually this should be in the same directory
as your ``manage.py``.

After that, you can immediately use a JSON view to get your git info - just add the
following to your urls.py:

```
from django_git.views import git_info

urlpatterns = [
    ...
    url(r'^git_info/$', git_info),
]
```

Also, if you want to print the git info to other views, there's a templatetag for this.
Just include ``django_git`` to your ``INSTALLED_APPS`` setting and in your templates you
could do:

```
{% load django_git_tags %}
{% get_git_info as gi %}

<ul>
    <li>Hash: {{ gi.hash }}</li>
    <li>Subject: {{ gi.subject }}</li>
    <li>Commiter date: {{ gi.commiter_date }}</li>
</ul>

```