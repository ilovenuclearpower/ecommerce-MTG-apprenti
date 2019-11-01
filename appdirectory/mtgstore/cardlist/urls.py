from django.conf.urls import url
from . import views

app_name = "cardlist_ns"
urlpatterns = [
    url(r'^.*$', views.search_card_list, name="search_card_list")
]