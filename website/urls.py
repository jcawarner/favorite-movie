from django.urls import path
from . import views
from members.views import log_out_user

urlpatterns = [
   path('', views.home, name='home'),
   path('popular/', views.popular, name='popular'),
   path('random_movies/', views.random_movies, name='random'),
   path('trending/', views.trending, name='trending'),
   path('now_playing/', views.now_playing, name='now_playing'),
   path('random_movies/movie/<str:id>', views.movie, name='movie'),
   path('random_movies/movie_saved/<str:id>', views.save_movie, name='save_movie'),
   path('home/account', views.account, name='account'),
   

]
