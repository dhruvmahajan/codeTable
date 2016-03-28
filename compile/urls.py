from django.conf.urls import url

urlpatterns = [
   
    url(r'^(?P<run_id>[\w]+)/$', 'compile.views.runCode', name='code'),
]
