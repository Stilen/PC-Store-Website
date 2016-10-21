from django.conf.urls import url
from django.contrib import admin
from . import views


app_name = 'products'


urlpatterns = [
    url(r'^$', views.products, name='products'),
    url(r'^(?P<id>[0-9]+)$', views.detail, name='detail'),
    url(r'^admin/', admin.site.urls),
]
