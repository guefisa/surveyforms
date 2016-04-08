from rest_framework import generics, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from django.contrib.auth.models import User

from .models import Muestra
from .serializers import MuestraSerializer, UserSerializer
from .permissions import IsOwnerOrReadOnly


class MuestraList(generics.ListCreateAPIView):
    queryset = Muestra.objects.all()
    serializer_class = MuestraSerializer

    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class MuestraDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Muestra.objects.all()
    serializer_class = MuestraSerializer

    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


@api_view(('GET',))
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'muestras': reverse('muestra-list', request=request, format=format)
    })