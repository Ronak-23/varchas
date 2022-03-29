from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .forms import EmailForm
from registration.models import TeamRegistration
import xlwt
from django.http import HttpResponse
from django.core.mail import send_mail
from accounts.models import UserProfile
from django.views.generic import CreateView


@login_required(login_url='login')
def dashboard(request):
    if not request.user.is_superuser:
        return render(request, "404")
    teams = TeamRegistration.objects.all()
    nteams = teams.count()
    users = UserProfile.objects.all()
    nusers = users.count()
    context = {'user': request.user, 'nteams': nteams, 'nusers': nusers}
    return render(request, 'adminportal/dashboard.html', context)


@login_required(login_url='login')
def dashboardTeams(request, sport=0):
    if not request.user.is_superuser:
        return render(request, "404")
    if request.method == 'POST' :
        sport= request.POST.get('sport')
    if sport == 0 or sport=='0':
        teams = TeamRegistration.objects.all().order_by('-captian__user__date_joined')
    elif sport == '11':
        teams = TeamRegistration.objects.all().exclude(college__iexact='IITJ').exclude(college__iexact='IIT Jodhpur').order_by('-captian__user__date_joined')
    else:
        teams = TeamRegistration.objects.filter(sport=sport).order_by('-captian__user__date_joined')
    users = UserProfile.objects.all()
    sports=['All', 'Athletics', 'Badminton', 'Basketball', 'Chess', 'Cricket', 'Football', 'Table Tenis', 'Tenis', 'Volleyball', 'Squash','Exclude IITJ']
    members={}
    for team in teams:
        member = []
        for user in users:
            if user.teamId== team:
                member.append(user.user.first_name)
        members[team.teamId]=(len(member))
    return render(request, 'adminportal/dashboardTeams.html', {'teams': teams, 'users': users, 'members': members, 'sports': sports, 'sport_select': sport})


@login_required(login_url='login')
def dashboardUsers(request):
    if not request.user.is_superuser:
        return render(request, "404")
    users = UserProfile.objects.all().order_by('-user__date_joined')
    return render(request, 'adminportal/dashboardUsers.html', {'users': users})


@login_required(login_url='login')
def downloadExcel(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="Varchas.xls"'
    wb = xlwt.Workbook(encoding='utf-8')

    ws = wb.add_sheet("Teams")
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.bold = True
    columns = ['TeamID', 'Sport', 'Captain', 'Captain no.', 'College', 'Members', 'Created on']
    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)
    font_style = xlwt.XFStyle()
    teams = TeamRegistration.objects.all().order_by('-captian__user__date_joined')
    users = UserProfile.objects.all()
    for team in teams:
        members = []
        for user in users:
            if user.teamId== team:
                members.append(user.user.first_name)
        row_num = row_num + 1
        ws.write(row_num, 0, team.teamId, font_style)
        ws.write(row_num, 1, team.get_sport_display(), font_style)
        ws.write(row_num, 2, team.captian.user.first_name, font_style)
        ws.write(row_num, 3, team.captian.phone, font_style)
        ws.write(row_num, 4, team.college, font_style)
        ws.write(row_num, 5, ", ".join(members), font_style)
        ws.write(row_num, 6, str(team.captian.user.date_joined)[:11])

    ws = wb.add_sheet("Users")
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.bold = True
    columns = ['Email', 'Name', 'Phone Number', 'Gender', 'College', 'teamId', 'Date Joined']
    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)
    font_style = xlwt.XFStyle()
    users = UserProfile.objects.all().order_by('-user__date_joined')
    for user in users:
        row_num = row_num + 1
        ws.write(row_num, 0, user.user.email, font_style)
        ws.write(row_num, 1, user.user.first_name+" "+user.user.last_name, font_style)
        ws.write(row_num, 2, user.phone, font_style)
        ws.write(row_num, 3, user.gender, font_style)
        ws.write(row_num, 4, user.college, font_style)
        ws.write(row_num, 5, user.teamId.teamId if user.teamId!=None else "" , font_style)
        ws.write(row_num, 7, str(user.user.date_joined)[:11])

    wb.save(response)
    return response


class sendMail(CreateView):
    form_class = EmailForm
    template_name = 'adminportal/email.html'
    success_url = '/admin'

    def form_valid(self, form):
        data = self.request.POST.copy()
        recipient = []
        if int(data['recipient']) < 10:
            teams = TeamRegistration.objects.all()
            for team in teams:
                if int(team.sport) == int(data['recipient']):
                    recipient.append(team.captian.user.email)
        elif int(data['recipient']) == 10:
            teams = TeamRegistration.objects.all()
            for team in teams:
                if team.captian:
                    message = '''<!DOCTYPE html> <html><body><p>{}</p>
                              <h3>{}</h3></body></html>'''.format(data['message'], "Your Team ID:" + team.teamId)
                    send_mail(data['subject'], message, 'noreply@varchas22.in',
                              [team.captian.user.email], fail_silently=False, html_message=message)
            return super(sendMail, self).form_valid(form)
        else:
            users = UserProfile.objects.all()
            for user in users:
                recipient.append(user.user.email)
                message = '''<!DOCTYPE html> <html><body>Hi {}!<br><p>{}</p>
                             <p>Team Varchas</p></body></html>'''.format(user.user.first_name, data['message'])
                send_mail(data['subject'], message, 'noreply@varchas22.in',
                          [user.user.email], fail_silently=False, html_message=message)
            return super(sendMail, self).form_valid(form)
        send_mail(data['subject'], data['message'], 'noreply@varchas22.in', recipient, fail_silently=False)
        return super(sendMail, self).form_valid(form)
