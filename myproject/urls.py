from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from rest_framework import routers
from myapp import urls
from django.views.generic import TemplateView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

router = routers.DefaultRouter()

urlpatterns = [
    path('admin/', admin.site.urls),
    url('api/', include(router.urls)),
    url('api/', include(urls, namespace='spots')),
    url('', TemplateView.as_view(template_name='index.html'), name='Home'),
]

urlpatterns += staticfiles_urlpatterns()
