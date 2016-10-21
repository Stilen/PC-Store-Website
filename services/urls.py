from django.conf.urls import url
from django.contrib import admin
from . import views


app_name = 'services'


urlpatterns = [
    url(r'^$', views.services, name='services'),
    url(r'^admin/', admin.site.urls),
]
