from django.urls import path
from . import views

# urlpatterns = [
#     path('', views.index, name='index')
# ]

urlpatterns = [
    path('helloworld/', views.index),
    path('bye/', views.bye),
    path('hello/', views.index),
    path('hi/',views.index)
]
