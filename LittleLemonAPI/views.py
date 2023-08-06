from rest_framework import generics, permissions, status
from rest_framework.response import Response
from django.contrib.auth.models import User, Group
from .models import MenuItem
from .serializers import *
from .permissions import *
from rest_framework.filters import OrderingFilter, SearchFilter

class MenuItemListCreateAPIView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    filter_backends = [OrderingFilter, SearchFilter]
    ordering_fields = ['title', 'price']
    search_fields = ['title', 'price']


    def get_permissions(self):
        if self.request.method == 'POST':
            return [CanManageMenuItemPermission()]
        return [permissions.AllowAny()]

class MenuItemRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

    def get_permissions(self):
        if self.request.method != 'GET':
            return [CanManageMenuItemPermission()]
        return [permissions.AllowAny()]
    
class ManagerListCreateAPIView(generics.ListCreateAPIView):
    queryset = User.objects.filter(groups__name='Manager')
    serializer_class = UserSerializer
    permission_classes = [CanManageUsers]

    def perform_create(self, serializer):
        user = serializer.save()

        manager_group = Group.objects.get(name='Manager')
        user.groups.add(manager_group)

class ManagerRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.filter(groups__name='Manager')
    serializer_class = UserSerializer
    permission_classes = [CanManageUsers]

class DeliveryCrewListCreateAPIView(generics.ListCreateAPIView):
    queryset = User.objects.filter(groups__name='Delivery Crew')
    serializer_class = UserSerializer
    permission_classes = [CanManageUsers]

    def perform_create(self, serializer):
        user = serializer.save()

        delivery_crew_group = Group.objects.get(name='Delivery Crew')
        user.groups.add(delivery_crew_group)

class DeliveryCrewRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.filter(groups__name='Delivery Crew')
    serializer_class = UserSerializer
    permission_classes = [CanManageUsers]

class CartListCreateDestroyAPIView(generics.ListCreateAPIView):
    serializer_class = CartSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Cart.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def delete(self, request, *args, **kwargs):
        Cart.objects.filter(user=self.request.user).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


