from django.conf.urls import patterns, url
from views import root

urlpatterns = patterns('',
    url(r'^$', root, name='root'),
)