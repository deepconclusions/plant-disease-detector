from django.urls import path
from . import views

urlpatterns = [
    path('single-prediction/', views.singlePrediction, name='single_prediction'),
    path('multiple-prediction/', views.multiplePrediction,
         name='multiple_prediction'),
]
