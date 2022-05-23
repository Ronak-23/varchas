from .views import TeamFormationView, removePlayerView, TeamViewSet
from rest_framework import routers
from django.urls import path, include
from django.conf.urls import url


app_name = 'registration'
router = routers.DefaultRouter()
router.register(r'teamsApi', TeamViewSet)
urlpatterns = [
    path('', include(router.urls)),
    path('team', TeamFormationView.as_view(), name='team'),
    url(r'removePlayer$', removePlayerView.as_view(), name='remove_player'),
    # url(r'team/(?P<username>[a-zA-Z0-9]+)$',TeamFormationView),
]
