from polls.models import Poll
from rest_framework import viewsets, permissions
from .serializers import PollSerializaer

class PollViewSet(viewsets.ModelViewSet):
    queryset = Poll.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = PollSerializaer