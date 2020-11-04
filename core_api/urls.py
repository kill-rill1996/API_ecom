from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views


urlpatterns = [
    path('items/', views.ItemViewSet.as_view({'get': 'list'})),
    path('items/<int:pk>/', views.ItemViewSet.as_view({'get': 'retrieve'})),

    # path('category/', views.CategoryListView.as_view()),
    # path('category/<int:pk>/', views.CategoryDetailView.as_view()),
    path('category/', views.CategoryViewSet.as_view({'get': 'list'})),
    path('category/<int:pk>/', views.CategoryViewSet.as_view({'get': 'retrieve'})),

    # path('order_item/', views.OrderItemView.as_view()),
    path('order/', views.OrderListView.as_view()),
    # path('order/remove/<int:pk>/', views.RemoveFromCart.as_view()),
    path('order/<int:pk>/', views.OrderDetailView.as_view()),

]