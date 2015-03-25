from django.conf.urls import patterns, url
import views

urlpatterns = patterns('',
    url(r'^$', views.root, name='root'),
    url(r'^get_result/$', views.get_result)
)