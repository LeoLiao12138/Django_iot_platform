from django.urls import path
from . import views

app_name = "[app_namespace]"
urlpatterns = [
    path('', views.index, name = 'index'),
    ]