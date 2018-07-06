from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^showtime/$', views.sayhello),

]