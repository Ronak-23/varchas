from django.urls import path
from .views import dashboardTeams, dashboardEsportsTeams
from .views import dashboardUsers, dashboard, downloadExcel, sendMail, updateScore, downloadEsportsExcel
from django.conf.urls import url

app_name = 'adminportal'

urlpatterns = [
    path('mail', sendMail.as_view(), name='mail'),
    url(r'teamsEsports$', dashboardEsportsTeams, name='deteams'),
    path(r'updateScore/(<str:sport>)/', updateScore, name='uscore'),
    url(r'teams$', dashboardTeams, name='dteams'),
    url(r'users$', dashboardUsers, name='dusers'),
    url(r'excel$', downloadExcel, name='teamInfo'),
    url(r'excelEsports$', downloadEsportsExcel, name='esportsInfo'),
    url('', dashboard, name='dashboard'),
]
