from django.urls import include, path

from . import views

app_name='autumn'
urlpatterns = [
    path('hello/', views.hello)
]
