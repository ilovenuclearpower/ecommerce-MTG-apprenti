from django.conf.urls import url
from . import views

app_name = "register_ns"

urlpatterns = [
    url(r'^$', views.register, name="register"),
]