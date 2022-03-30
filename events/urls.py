from .views import CreateMatch, CricketViewSet, FootballViewSet, VolleyballViewSet, ChessViewSet, SquashViewSet, TT, badminton, cricket, squash, football, volleyball, chess, athletics, informals, tennis, basketball
from django.urls import path, include
from rest_framework import routers

app_name = 'events'

router = routers.DefaultRouter()
router.register(r'cricketApi', CricketViewSet)
router.register(r'footballApi', FootballViewSet)
router.register(r'volleyballApi', VolleyballViewSet)
router.register(r'chessApi', ChessViewSet)
router.register(r'squashApi', SquashViewSet)

urlpatterns = [
    path('add', CreateMatch.as_view(), name='add_match'),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('cricket', cricket, name='cricket'),
    path('football', football, name='football'),
    path('volleyball', volleyball, name='volleyball'),
    path('chess', chess, name='chess'),
    path('TT', TT, name='TT'),
    path('badminton', badminton, name='badminton'),
    path('tennis', tennis, name='tennis'),
    path('athletics', athletics, name='athletics'),
    path('informals', informals, name='informals'),
    path('basketball', basketball, name='basketball')
]
