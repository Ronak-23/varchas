from django.views.generic import FormView
from .forms import MatchForm
from .models import Match, Event, Cricket, Volleyball, Football, BasketBall, Chess, Squash, Badminton, TT, Tennis
from django.contrib import messages
from rest_framework import viewsets
from .serializers import CricketSerializer, FootballSerializer, VolleyballSerializer, ChessSerializer, SquashSerializer, BadmintonSerializer, TTSerializer, TennisSerializer
from rest_framework import permissions
from django.shortcuts import render


class CreateMatch(FormView):
    template_name = 'events/add_match.html'
    form_class = MatchForm
    success_url = '/events/add'

    def form_valid(self, form):
        data = self.request.POST.copy()
        game_ch = Event.EVENT_CHOICES[int(data['event']) - 1][1][:2].upper()
        type_ch = Match.MATCH_CHOICES[int(data['match_type']) - 1][1][:2].upper()
        data['event_id'] = game_ch + '-' + type_ch + '-' + data['team1'][:2].upper() + data['team2'][:2].upper()
        form = MatchForm(data)
        if Match.objects.filter(event_id=data['event_id']).exists():
            message = "You are already in team {}".format(data['event_id'])
        else:
            message = "Match created with Match ID {}".format(data['event_id'])
            obj = form.save()
            obj.event_id = data['event_id']
            obj.save()
            CreateMatch.create_match(obj, **form.cleaned_data)
        messages.success(self.request, message)
        return super(CreateMatch, self).form_valid(form)

    @staticmethod
    def create_match(match=None, **kwargs):
        if kwargs['event'] == '2' or kwargs['event'] == '9':
            sport = Volleyball(match=match)
        elif kwargs['event'] == '6' or kwargs['event'] == '7' or kwargs['event'] == '8':
            sport = Football(match=match)
        elif kwargs['event'] == '5':
            sport = Cricket(match=match)
        elif kwargs['event'] == '3':
            sport = BasketBall(match=match)
        elif kwargs['event'] == '4':
            sport = Chess(match=match)
        sport.save()

    def get_template_names(self):
        if not self.request.user.is_superuser:
            return "main/error_404.html"
        return super().get_template_names()


class CricketViewSet(viewsets.ModelViewSet):
    queryset = Cricket.objects.all()
    serializer_class = CricketSerializer
    permission_classes = [permissions.IsAdminUser]


class FootballViewSet(viewsets.ModelViewSet):
    queryset = Football.objects.all()
    serializer_class = FootballSerializer
    permission_classes = [permissions.IsAdminUser]


class VolleyballViewSet(viewsets.ModelViewSet):
    queryset = Volleyball.objects.all()
    serializer_class = VolleyballSerializer
    permission_classes = [permissions.IsAdminUser]


class ChessViewSet(viewsets.ModelViewSet):
    queryset = Chess.objects.all()
    serializer_class = ChessSerializer
    permission_classes = [permissions.IsAdminUser]


class SquashViewSet(viewsets.ModelViewSet):
    queryset = Squash.objects.all()
    serializer_class = SquashSerializer
    permission_classes = [permissions.IsAdminUser]


class BadmintonViewSet(viewsets.ModelViewSet):
    queryset = Badminton.objects.all()
    serializer_class = BadmintonSerializer
    permission_classes = [permissions.IsAdminUser]


class TTViewSet(viewsets.ModelViewSet):
    queryset = TT.objects.all()
    serializer_class = TTSerializer
    permission_classes = [permissions.IsAdminUser]

class TennisViewSet(viewsets.ModelViewSet):
    queryset = Tennis.objects.all()
    serializer_class = TennisSerializer
    permission_classes = [permissions.IsAdminUser]


def cricket(request):
    return render(request, 'events/cricket.html')


def football(request):
    return render(request, 'events/football.html')


def volleyball(request):
    return render(request, 'events/volleyball.html')


def chess(request):
    return render(request, 'events/chess.html')


def squash(request):
    return render(request, 'events/squash.html')


def TT(request):
    return render(request, 'events/TT.html')


def badminton(request):
    return render(request, 'events/badminton.html')


def tennis(request):
    return render(request, 'events/tennis.html')


def athletics(request):
    return render(request, 'events/athletics.html')


def informals(request):
    return render(request, 'events/informals.html')


def basketball(request):
    return render(request, 'events/basketball.html')

def valorant(request):
    return render(request, 'events/valorant.html')

def bgmi(request):
    return render(request, 'events/bgmi.html')