from django.urls import path
from .views import dashboardTeams, dashboardEsportsTeams
from .views import dashboardUsers, dashboard, downloadExcel, sendMail
from django.conf.urls import url

app_name = 'adminportal'

urlpatterns = [
    path('mail', sendMail.as_view(), name='mail'),
    url(r'teams$', dashboardEsportsTeams, name='deteams'),
    url(r'teams$', dashboardTeams, name='dteams'),
    url(r'users$', dashboardUsers, name='dusers'),
    url(r'excel$', downloadExcel, name='teamInfo'),
    url('', dashboard, name='dashboard'),
]
