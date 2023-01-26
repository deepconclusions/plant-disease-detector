from django.urls import path
from . import views

urlpatterns = [
    path('prediction/', views.getPredictions, name='corn_prediction'),
]
