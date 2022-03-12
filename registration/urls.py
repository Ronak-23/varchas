from .views import TeamFormationView, removePlayerView
from django.urls import path
from django.conf.urls import url


app_name = 'registration'

urlpatterns = [
    path('team', TeamFormationView.as_view(), name='team'),
    url(r'removePlayer$', removePlayerView.as_view(), name='remove_player'),
    # url(r'team/(?P<username>[a-zA-Z0-9]+)$',TeamFormationView),
]
