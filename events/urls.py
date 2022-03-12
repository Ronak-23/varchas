from .views import CreateMatch, CricketViewSet, FootballViewSet, VolleyballViewSet, ChessViewSet, SquashViewSet
from django.urls import path, include
from rest_framework import routers

app_name = 'events'

router = routers.DefaultRouter()
router.register(r'cricket', CricketViewSet)
router.register(r'football', FootballViewSet)
router.register(r'volleyball', VolleyballViewSet)
router.register(r'chess', ChessViewSet)
router.register(r'squash', SquashViewSet)

urlpatterns = [
    path('add', CreateMatch.as_view(), name='add_match'),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
