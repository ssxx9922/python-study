from django.urls import path

from . import views

urlpatterns = [
    path('list/',views.list),
    path('details/', views.details),
    path('write/', views.write),
    path('delete/', views.delete),
]