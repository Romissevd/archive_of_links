from django.urls import path

from . import views

urlpatterns = [
    path('category/', views.CategoryView.as_view(), name='category'),
    path('category/add/', views.CreateCategoryView.as_view(), name='add_category')
]
