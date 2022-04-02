from .models import Cricket, Football, Volleyball, Chess, Squash, Badminton, TT, Tennis
from rest_framework import serializers


class CricketSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cricket
        fields = ['match', 'run1', 'run2', 'wicket1', 'wicket2', 'overs1', 'overs2']


class FootballSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Football
        fields = ['match', 'score1', 'score2', ]


class VolleyballSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Volleyball
        fields = ['match', 'score1', 'score2', 'setNo']


class ChessSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Chess
        fields = ['match', 'score1', 'score2', ]


class SquashSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Squash
        fields = ['match', 't1s1', 't2s1', 't1s2', 't2s2', 't1s3', 't2s3', 't1s4', 't2s4', 't1s5', 't2s5', 't1sw', 't2sw']


class BadmintonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Badminton
        fields = ['match', 't1s1', 't2s1', 't1s2', 't2s2', 't1s3', 't2s3', 't1sw', 't2sw']


class TTSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TT
        fields = ['match', 't1s1', 't2s1', 't1s2', 't2s2', 't1s3', 't2s3', 't1sw', 't2sw']


class TennisSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tennis
        fields = ['match', 't1s1', 't2s1', 't1s2', 't2s2', 't1s3', 't2s3', 't1sw', 't2sw']