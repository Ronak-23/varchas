from django.views.generic import CreateView
from .forms import TeamRegistrationForm, RemovePlayerForm
from django.shortcuts import get_object_or_404
from accounts.models import UserProfile
from django.http import HttpResponse
from random import random
from .models import TeamRegistration
from django.core.mail import send_mail
from django.views.generic import FormView
from django.contrib.auth.models import User


class TeamFormationView(CreateView):
    form_class = TeamRegistrationForm
    template_name = 'registration/team.html'
    success_url = '/account/myTeam'

    def form_valid(self, form):
        user = self.request.user
        if user is not None:
            form = TeamRegistrationForm(self.request.POST)
            user = get_object_or_404(UserProfile, user=user)
            if user.teamId is not None:
                message = "You are already in team {}".format(user.teamId)
                message += "\nYou have to register again to join another team. \nContact Varchas administrators."
                return HttpResponse(message, content_type="text/plain")
            team = form.save()
            if team.sport == '5':
                message = "Registration for Cricket has been closed."
                team.delete()
                return HttpResponse(message, content_type="text/plain")
            if ((team.sport == '3' or team.sport == '9') and user.gender == 'M'):
                message = "Registration for Volleyball(M) and basketball(M) has been closed."
                team.delete()
                return HttpResponse(message, content_type="text/plain")
            if team.sport == '6':
                message = "Registration for Football has been closed."
                team.delete()
                return HttpResponse(message, content_type="text/plain")
            if team.sport == '4':
                message = "Registration for Chess will reopen soon."
                team.delete()
                return HttpResponse(message, content_type="text/plain")
            spor = TeamRegistration.SPORT_CHOICES[int(team.sport)-1][1][:3]
            team.teamId = "VA-" + spor[:3].upper() + '-' + user.user.username[:3].upper() + "{}".format(int(random()*100))
            team.captian = user
            team.save()
            user.teamId = team
            user.save()

            message = '''<!DOCTYPE html> <html><body>Hi {}!<br>You have successfully registered for Varchas2022.<br>Your teamId is: <b>{}</b><br>
                          Check your team details here: <a href="http://varchas22.in/account/myTeam">varchas22.in/account/myTeam</a><p>Vigour| Valour| Victory.</p></body></html>'''.format(user.user.first_name, user.teamId)
            send_mail('Varchas Team Created', message, 'noreply@varchas22.in', [team.captian.user.email],
                      fail_silently=False, html_message=message)

            return super(TeamFormationView, self).form_valid(form)
        return HttpResponse("404")


# @login_required(login_url="login")
class removePlayerView(FormView):
    form_class = RemovePlayerForm
    template_name = 'registration/remove_player.html'
    success_url = '/account/myTeam'

    def form_valid(self, form):
        user = get_object_or_404(UserProfile, user=self.request.user)
        teamId = user.teamId
        if user.teamId is None:
            return HttpResponse("You must registered in a team to complete this operation.")
        team = get_object_or_404(TeamRegistration, teamId=teamId)
        if user != team.captian:
            return HttpResponse('Only captain can remove a player in a team')
        user = get_object_or_404(User, email=form['player'].value())
        user = get_object_or_404(UserProfile, user=user)
        if user.teamId != teamId:
            return HttpResponse("Sorry this player is not in the team")
        user.teamId = None
        user.save()
        return super(removePlayerView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(removePlayerView, self).get_context_data(**kwargs)
        user = get_object_or_404(UserProfile, user=self.request.user)
        users = UserProfile.objects.filter(teamId=user.teamId)
        team = get_object_or_404(TeamRegistration, teamId=user.teamId)
        userList = []
        for i in users:
            userList.append(i)
        userList.remove(team.captian)
        context['players'] = userList
        return context
