from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [

    path('task/<str:id>', views.taskDetail),
    path('', views.taskManager),
    path('user/', views.userManager)
    
]
