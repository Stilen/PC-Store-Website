from django.conf.urls import url
from django.contrib import admin
from . import views


app_name = 'about'


urlpatterns = [
    url(r'^$', views.about, name='about'),
    url(r'^admin/', admin.site.urls),
]
