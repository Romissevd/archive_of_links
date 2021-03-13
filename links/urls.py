from django.urls import path

from . import views

urlpatterns = [
    path('', views.LinkView.as_view()),
]