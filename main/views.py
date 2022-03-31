from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
# from .utils import SiteAccessMixin
from .models import NavBarSubOptions, OurTeam, HomeEventCard
from django.shortcuts import get_object_or_404, render
from accounts.models import UserProfile
from rest_framework import viewsets
from .serializers import OurTeamSerializer
from rest_framework import permissions


class IndexView(TemplateView):

    template_name = 'main/index.html'

    def get_context_data(self, **kwargs):
        if self.request.user.username != "":
            userprofile = get_object_or_404(UserProfile, user=self.request.user)
        context = super(IndexView, self).get_context_data(**kwargs)
        context['event_list'] = HomeEventCard.objects.all
        if self.request.user.username != "":
            context['userprofile'] = userprofile
            context['page'] = "home"
        return context


class NavBarSubOptionsPageView(DetailView):
    template_name = 'main/navbarsuboptionpage.html'
    model = NavBarSubOptions

    def get_context_data(self, **kwargs):
        context = super(NavBarSubOptionsPageView, self).get_context_data()
        return context

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        if self.object.use_custom_html:
            self.template_name = self.object.custom_html
        else:
            self.template_name = 'main/navbarsuboptionpage.html'
        return self.render_to_response(context)


class OurTeamView(TemplateView):
    template_name = 'main/our_team.html'
    model = OurTeam

    def get_context_data(self, **kwargs):
        context = super(OurTeamView, self).get_context_data(**kwargs)
        context["our_team"] = OurTeam.objects.all
        context['page'] = "ourTeam"
        return context


def comingSoon(request):
    return render(request, 'main/comingSoon.html')


def error_404(request, exception):
    return render(request, 'main/error_404.html', status=404)


def error_500(request):
    return render(request, 'main/error_500.html', status=500)


class OurTeamViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = OurTeam.objects.all()
    serializer_class = OurTeamSerializer
    permission_classes = [permissions.IsAdminUser]

def aboutus(request):
    return render(request, 'main/aboutus.html')


def payment(request):
    if not request.user.is_authenticated:
        return render(request, "404")
    if request.user.username != "":
        userprofile = get_object_or_404(UserProfile, user=request.user)
    context = {}
    sports=['All', 'Athletics', 'Badminton', 'Basketball', 'Chess', 'Cricket', 'Football', 'Table Tennis', 'Tennis', 'Volleyball', 'Badminton-mixed doubles']
    context['userprofile'] = userprofile
    context['page'] = "payment"
    if(userprofile.teamId==None):
        context['amount']= None
    else:
        context['captain'] = userprofile.teamId.captian==userprofile
        context['amount']= 0
        sport=userprofile.teamId.sport
        context['sports'] = sports[int(sport)]
        if(sport=='1' and userprofile.teamId.captian==userprofile):
            context['amount'] = 100
        elif(sport=='2' and userprofile.teamId.captian==userprofile and userprofile.gender== 'M'):
            context['amount'] = 1000
        elif(sport=='2' and userprofile.teamId.captian==userprofile and userprofile.gender== 'F'):
            context['amount'] = 600
        elif((sport=='3' or sport=='9') and userprofile.teamId.captian==userprofile and userprofile.gender== 'M'):
            context['amount'] = 2000
        elif((sport=='3' or sport=='9') and userprofile.teamId.captian==userprofile and userprofile.gender== 'F'):
            context['amount'] = 1000
        elif(sport=='4'):
            context['amount']=0
        elif((sport=='5' or sport=='6') and userprofile.teamId.captian==userprofile):
            context['amount'] = 3500
        elif((sport=='7' or sport=='8') and userprofile.teamId.captian==userprofile and userprofile.gender== 'M'):
            context['amount'] = 1000
        elif((sport=='7' or sport=='8') and userprofile.teamId.captian==userprofile and userprofile.gender== 'F'):
            context['amount'] = 600
        elif(sport=='10' and userprofile.teamId.captian==userprofile):
            context['amount'] = 400
    if(userprofile.accommodation_required == 'Y'):
        
        context['accommodation'] = 1099
    else:
        context['accommodation'] = 0
    if(context['captain']):
        if(context['amount']==None):
            userprofile.amount_required = context['accommodation']
        else:
            userprofile.amount_required = context['amount'] + context['accommodation']
    return render(request, 'main/payment.html', context)


def paymentCompletion(request):
    return render(request, 'main/paymentCF.html')


def privacy(request):
    return render(request, 'privacy.html')
