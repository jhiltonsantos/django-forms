from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('add_reporter/', views.add_reporter, name='add_reporter'),
    path('list_reporters/', views.list_reporters, name='list_reporters'),
    path('add_article/', views.add_article, name='add_article'),
    path('list_articles/', views.list_articles, name='list_articles'),
    path('add_client/', views.add_client, name='add_client'),
    path('list_clients/', views.list_clients, name='list_clients'),
    path('add_product/', views.add_product, name='add_product'),
    path('list_products/', views.list_products, name='list_products'),
    path('add_purchase/', views.add_purchase, name='add_purchase'),
    path('list_purchases/', views.list_purchases, name='list_purchases'),
    path('add_actor/', views.add_actor, name='add_actor'),
    path('list_actors/', views.list_actors, name='list_actors'),
    path('add_movie/', views.add_movie, name='add_movie'),
    path('list_movies/', views.list_movies, name='list_movies'),

]
