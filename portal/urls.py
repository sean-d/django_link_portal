from django.urls import path
from .views import portal_about, portal_add_category, portal_add_page, portal_index, portal_show_category


app_name = "portal"

urlpatterns = [
    path("", portal_index, name="portal_index"),
    path("about/", portal_about, name="portal_about"),
    path("add_category/", portal_add_category, name="portal_add_category"),
    path("category/<slug:slug>/", portal_show_category, name="portal_show_category"),
    path("category/<slug:slug>/add_page/", portal_add_page, name="portal_add_page"),
]
