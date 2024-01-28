from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework_api_key.permissions import HasAPIKey

from core.models import Riddle
from core.serializers import RiddleSerializer


class RiddleViewSet(viewsets.ModelViewSet):
    """
    A viewset for performing riddle CRUD operations.
    """
    serializer_class = RiddleSerializer
    queryset = Riddle.objects.all()

    @action(detail=True, methods=['post'], permission_classes=[HasAPIKey])
    def riddle_me_this(self, request, pk=None):
        riddle = self.get_object()
        data = RiddleSerializer(riddle).data
        data.update(request.data)
        serializer = RiddleSerializer(data=data)

        if serializer.is_valid():
            riddle.chosen_answer = serializer.validated_data['chosen_answer']
            riddle.save()
            return Response(
                {'correct': riddle.chosen_answer == riddle.correct_answer}
            )
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
