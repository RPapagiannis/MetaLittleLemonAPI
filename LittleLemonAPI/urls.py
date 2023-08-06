from django.urls import path
from .views import *

urlpatterns = [
    path('menu-items', MenuItemListCreateAPIView.as_view(), name='menu-items'),
    path('menu-items/<int:pk>', MenuItemRetrieveUpdateDestroyAPIView.as_view(), name='menu-item-detail'),
    path('groups/manager/users', ManagerListCreateAPIView.as_view(), name='managers'),
    path('groups/manager/users/<int:pk>', ManagerRetrieveUpdateDestroyAPIView.as_view(), name='manager-detail'),
    path('groups/delivery-crew/users', DeliveryCrewListCreateAPIView.as_view(), name='delivery-crew'),
    path('groups/delivery-crew/users/<int:pk>', DeliveryCrewRetrieveUpdateDestroyAPIView.as_view(), name='delivery-crew-detail'),
    path('cart', CartListCreateDestroyAPIView.as_view(), name='cart'),
]