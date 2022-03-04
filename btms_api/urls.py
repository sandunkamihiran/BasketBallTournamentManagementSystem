from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TeamViewSet, CoachViewSet, PlayerViewSet, RoundViewSet, MatchViewSet, UserViewSet, \
    LogoutView
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register('teams', TeamViewSet, basename='teams')
router.register('coaches', CoachViewSet, basename='coaches')
router.register('players', PlayerViewSet, basename='players')
router.register('rounds', RoundViewSet, basename='rounds')
router.register('matches', MatchViewSet, basename='matches')
router.register('users', UserViewSet, basename='user-list')
# router.register('login', LoginView, basename='login')


urlpatterns = [
    path('btms_api/', include(router.urls)),
    path('btms_api/logout/', LogoutView.as_view(), name='logout'),
    path('btms_api/login/', obtain_auth_token, name='btms_api/login/')
]
