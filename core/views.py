from rest_framework import viewsets

from core.models import Riddle
from core.serializers import RiddleSerializer


class RiddleViewSet(viewsets.ModelViewSet):
    """
    A viewset for performing riddle CRUD operations.
    """
    serializer_class = RiddleSerializer
    queryset = Riddle.objects.all()
