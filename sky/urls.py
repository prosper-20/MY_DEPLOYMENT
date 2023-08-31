from django.urls import path
from . import views

urlpatterns = [
    path("", views.homepage, name="home"),
    path("category/", views.category, name="category"),
    path("contact/", views.contact, name="contact"),
    path("about/", views.about, name="about"),
    path("<slug:slug>/", views.detail, name="detail"),
]