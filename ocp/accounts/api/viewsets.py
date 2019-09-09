from ..models import User
from rest_framework import viewsets
from .serializers import UserSerializer

from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAdminUser, IsAuthenticated, AllowAny


# Create API methods/verbs automatic
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = (IsAdminUser, )
