from django.conf.urls import url

urlpatterns = [
   
    url(r'^(?P<run_id>[0-9]+)/$', 'compile.views.runCode', name='code'),
]
