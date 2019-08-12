from django.conf.urls import url
from .views import SpotListApiView, SpotRetrieveApiView

app_name = 'myapp'
urlpatterns = [
    url(r'^spots/$', SpotListApiView.as_view()),
    url(r'^spots/(?P<spot_id>\w+)/?$', SpotRetrieveApiView.as_view()),
]