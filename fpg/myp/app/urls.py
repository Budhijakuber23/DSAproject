from django.contrib import admin
from django.urls import path
from app import views


urlpatterns = [
    path('', views.index, name='index'),
    path('array/', views.array, name='array'),
    path('backt/', views.backt, name='backt'),
    path('bsearch/', views.bsearch, name='bsearch'),
    path('greedy/', views.greedy, name='greedy'),
    path('llist/', views.llist, name='llist'),
    path('heap/', views.heap, name='heap'),
    path('stque/', views.stque, name='stque'),
    path('str/', views.str, name='str'),
    path('bt/', views.bt, name='bt'),
    path('bst/', views.bst, name='bst'),
    path('grp/', views.grp, name='grp'),
    path('dp/', views.dp, name='dp'),
    path('trie/', views.trie, name='trie'),

]
