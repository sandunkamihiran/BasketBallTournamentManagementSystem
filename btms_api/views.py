from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.exceptions import ValidationError
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .permission import IsAdminUser, IsAdminOrCoachUser
from .serializers import TeamSerializer, CoachSerializer, PlayerSerializer, RoundSerializer, MatchSerializer, \
    UserSerializer
from .models import Team, Coach, Player, Round, Match, User
import numpy as np


class TeamViewSet(viewsets.ModelViewSet):

    serializer_class = TeamSerializer
    queryset = Team.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminUser]


class CoachViewSet(viewsets.ModelViewSet):

    serializer_class = CoachSerializer
    queryset = Coach.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminUser]


class PlayerViewSet(viewsets.ModelViewSet):

    serializer_class = PlayerSerializer
    authentication_classes = [TokenAuthentication]

    def get_permissions(self):
        permission_classes = []
        if self.action == 'create':
            permission_classes = [IsAdminUser]
        elif self.action == 'list':
            permission_classes = [IsAdminOrCoachUser]
        elif self.action == 'retrieve' or self.action == 'update' or self.action == 'partial_update':
            permission_classes = [IsAdminOrCoachUser]
        elif self.action == 'destroy':
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]

    def get_queryset(self):
        queryset = Player.objects.all()

        query_params = self.request.query_params
        team = query_params.get('team')
        percentile = query_params.get('percentile')

        if team:
            try:
                queryset = queryset.filter(team__id=team)
                if percentile:
                    queryset = self.filter_queryset_by_percentile(queryset, percentile)
            except Exception:
                raise ValidationError(
                    'Error(s) occurred when filtering with query param. Please check for invalid query params')

        return queryset

    def filter_queryset_by_percentile(self, queryset, percentile):
        query_arr = queryset.values_list('average_score', flat=True)
        arr = list(query_arr)
        calculated_percentile = np.percentile(arr, float(percentile))
        queryset = queryset.filter(average_score__gte=calculated_percentile)
        return queryset


class RoundViewSet(viewsets.ModelViewSet):

    serializer_class = RoundSerializer
    queryset = Round.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminUser]


class MatchViewSet(viewsets.ModelViewSet):

    serializer_class = MatchSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Match.objects.all()
        query_params = self.request.query_params
        round_param = query_params.get('round')

        if round_param:
            try:
                queryset = queryset.filter(round=int(round_param))
            except Exception:
                raise ValidationError(
                    'Error(s) occurred when filtering with query param. Please check for invalid query params')
        return queryset


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminUser]


class LoginView(viewsets.ViewSet):
    serializer_class = AuthTokenSerializer

    def create(self, request):
        return ObtainAuthToken().post(request)


class LogoutView(APIView):
    def get(self, request):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)
