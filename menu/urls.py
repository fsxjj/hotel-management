from django.urls import path
from . import views

urlpatterns = [
    path("categories/", views.CategoryListCreateAPIView.as_view(), name="category-list-create"),
    path("categories/<int:pk>/", views.CategoryDetailAPIView.as_view(), name="category-detail"),
    path("items/", views.MenuItemListCreateAPIView.as_view(), name="menuitem-list-create"),
    path("items/<int:pk>/", views.MenuItemDetailAPIView.as_view(), name="menuitem-detail"),
]

