from django.urls import path

from . import views

urlpatterns = [
    path('', views.matchPlayedPerYear, name=''),
    path('extra-runs', views.extraRuns, name=''),
    path('economical-bowlwers', views.economicalBowlers, name='')
]

