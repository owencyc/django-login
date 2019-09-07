from django.urls import include, path

from . import views

app_name = 'autumn'
urlpatterns = [
    path('hello/', views.hello),
    path('getData/', views.getData),
    path('addIntro/', views.addIntro),
    path('addIntro2/', views.addIntro2),
    path('addSkill/', views.addSkill),
    path('addVerse/', views.addVerse),
    path('delVerse/', views.delVerse),
    path('delSkill/', views.delSkill),
]
