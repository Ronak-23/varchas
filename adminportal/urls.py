from django.urls import path
from .views import dashboardTeams
from .views import dashboardUsers, dashboard, downloadExcel, sendMail
from django.conf.urls import url

app_name = 'adminportal'

urlpatterns = [
    path('mail', sendMail.as_view(), name='mail'),
    url(r'teams$', dashboardTeams, name='dteams'),
    url(r'users$', dashboardUsers, name='dusers'),
    url(r'excel$', downloadExcel, name='teamInfo'),
    url('', dashboard, name='dashboard'),
]
