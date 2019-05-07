from django.urls import path

from . import views

urlpatterns = [
    path('', views.scores, name='scores'),
    path('<int:score_id>/', views.index, name='index'),
    path('<int:score_id>/submit/', views.submit, name="submit")
]
