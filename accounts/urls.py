from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^create-account/$', views.create_account, name='create_account'),
    url(r'^apply/$', views.apply_id, name='apply'),

]
