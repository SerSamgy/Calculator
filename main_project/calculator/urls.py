from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
import views

urlpatterns = patterns('',
    url(r'^$', views.root, name='root'),
    url(r'^api/get_result/$', views.get_result),
    url(r'^api/set_expression/$', views.set_expression),
)

urlpatterns = format_suffix_patterns(urlpatterns)