from django.urls import path

from . import views

urlpatterns = [
    path('api/product/create/', views.ProductListCreate.as_view()),
    path('api/product/', views.ProductListView.as_view()),
]
