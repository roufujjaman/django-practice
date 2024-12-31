from django.contrib.auth.models import Group, User
from rest_framework import permissions, viewsets

from api.serializer import GroupSerializer, UserSerializer
# Create your views here.


from rest_framework.response import Response
from rest_framework.decorators import api_view

class UserViewSet(viewsets.ModelViewSet):

    queryset = User.objects.all().order_by("-date_joined")
    serializer_class = UserSerializer
    permission_classes = [
        permissions.IsAuthenticated
    ]

class GroupViewSet(viewsets.ModelViewSet):

    queryset = Group.objects.all().order_by("name")
    serializer_class = GroupSerializer
    permission_classes = [
        permissions.IsAuthenticated
    ]

@api_view(["GET"])
def test(request):
    data = {"name": "roufujjaman"}
    return Response(data)