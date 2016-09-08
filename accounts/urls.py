from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^index/$', views.index, name='index'),
    url(r'^$', views.user_login, name='login'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^create-account/$', views.create_account, name='create_account'),
    url(r'^apply/$', views.apply_id, name='apply'),
    url(r'^my-application/$', views.view_application_status, name='application'),
    url(r'^contact-support/$', views.contact_support, name='support'),
    url(r'^about/$', views.about, name='about'),

]
