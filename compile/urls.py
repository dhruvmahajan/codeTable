from django.conf.urls import url

urlpatterns = [
   
    url(r'^$', 'compile.views.runNewCode', name='newCode'),
    url(r'^(?P<run_id>[\w]+)/$', 'compile.views.runCode', name='code'),
]
