from django.urls import path
from .views import IndexView, NavBarSubOptionsPageView, OurTeamView, comingSoon, OurTeamViewSet, aboutus, payment, paymentCompletion, privacy
from django.conf.urls import url, include
from rest_framework import routers

app_name = 'main'

router = routers.DefaultRouter()
router.register(r'team', OurTeamViewSet)

urlpatterns = [
    url(r'^comingSoon$', comingSoon, name='comingSoon'),
    path('', IndexView.as_view(), name='home'),
    path('OurTeam', OurTeamView.as_view(), name='OurTeam'),
    path('aboutus', aboutus, name='aboutus'),
    path('payment', payment, name='payment'),
    path('paymentCF', paymentCompletion, name='paymentCF'),
    path('privacy', privacy, name='privacy'),
    path('<slug:slug>', NavBarSubOptionsPageView.as_view(),
         name='navbarsuboptionpage'),
    path('mainapi/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
