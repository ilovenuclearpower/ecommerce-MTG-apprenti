from django.conf.urls import url
from . import views

app_name = "cart_ns"
urlpatterns = [
    url(r'^$', views.show_cart, name="show_cart"),
]