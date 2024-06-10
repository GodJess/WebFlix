from django.urls import path
from . import views


urlpatterns = [
    path('', views.index , name="index"),
    path('main/', views.main , name="main"),
    path('details/', views.details, name ="details"),
    path('details-content/', views.details_content, name="details_content"),
    path("play_video/", views.play_video, name= "play_video"),
    path('add_video/', views.add_video, name = "add_video"),
    path("fantazy", views.fantazy, name="fantazy"),
    path("science", views.science, name = "science"),
    path("kriminal", views.kriminal , name = "kriminal"),
    path("horror", views.horror, name = "horror"),
    path("multfilm", views.multfilm , name = 'multfilm'),
    path("dram", views.dram , name="dram"),
    path("serial", views.serial , name="serial"),
    path("film", views.film , name="film"),
    path("comedy", views.comedy , name="comedy"),
    path("search", views.search, name = "search"),
    path("addcomment", views.addcomment , name = "addcomment")
]