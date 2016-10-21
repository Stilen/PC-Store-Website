from django.conf.urls import url
from django.contrib import admin
from . import views


app_name = 'contact'


urlpatterns = [
    url(r'^$', views.contact, name='contact'),
    url(r'^admin/', admin.site.urls),
]
