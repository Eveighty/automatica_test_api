from django.urls import path

from api import views

urlpatterns = [
    path('retailpoints/', views.retail_points, name='retail-points'),
    path('visit/', views.visit, name='visit'),
]