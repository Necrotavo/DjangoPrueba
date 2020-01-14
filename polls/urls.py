from rest_framework import routers
from .api import PollViewSet
from django.urls import path
from . import views

router = routers.DefaultRouter()
router.register('api/polls', PollViewSet, 'polls')
urlpatterns = router.urls