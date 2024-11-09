from django.urls import path
from . import views
urlpatterns = [
    path('produtos/', views.getProdutos),
    path('produtos/<int:pk>/', views.getProdutoById),
]