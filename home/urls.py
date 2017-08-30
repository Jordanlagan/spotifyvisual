from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^callback$', views.callback, name='callback'),
    url(r'^login$', views.login, name='login'),
    url(r'^refresh_token$', views.refresh_token, name='refresh_token'),
]
