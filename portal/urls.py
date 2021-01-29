from django.urls import path
from .views import portal_about, portal_index, portal_show_category


app_name = "portal"

urlpatterns = [
    path("", portal_index, name="portal_index"),
    path("about/", portal_about, name="portal_about"),
    path("category/<slug:slug>/", portal_show_category, name="portal_show_category"),
]
