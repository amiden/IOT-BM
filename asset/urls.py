from django.conf.urls import url
from . import views
from django.contrib import admin
app_name = 'asset'
admin.autodiscover()
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9a-z]{8}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{12})/$', views.DevInfoView.as_view(), name='dev_info'),

]