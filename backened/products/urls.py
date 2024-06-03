from django.urls import path
from . import views

urlpatterns=[
  path('<int:pk>/', views.ProductDetailApiView.as_view()),
  path('create-products', views.ProductCreateAPIView.as_view()),
  path('list-products/',views.ProductListAPIView.as_view()),
  path('list-create/',views.ProductListCreateAPIView.as_view()),
  path('funcBased/',views.FuncBasedProduct_all_view),
   path('funcBased/<int:pk>/', views.FuncBasedProduct_all_view),
]