from rest_framework import status
from rest_framework.test import APITestCase
from .models import Team, Coach, Round, Match, Player, User
from django.contrib.auth.models import Group


class TeamAPITests(APITestCase):

    def setUp(self):
        group = Group(name='admin')
        group.save()
        user = User(first_name='Test', last_name='User', username='testuser', email='test@gmail.com', groups=group)
        user.save()
        team = Team(name='Team A', average_score=145.6)
        team.save()

    def testCreateTeam(self):
        """
        Ensure we can create/post Team objects through API.
        """
        team = {'name': 'Test Team A', 'average_score': 100.5}
        user = User.objects.get(username='testuser')
        self.client.force_authenticate(user=user)
        response = self.client.post('/btms_api/teams/', team, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Team.objects.count(), 2)

    def testCreateTeamUnauthorized(self):
        """
        Ensure we can create/post Team objects through API.
        """
        team = {'name': 'Test Team A', 'average_score': 100.5}
        response = self.client.post('/btms_api/teams/', team, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def testGetTeam(self):
        """
        Ensure we can get Team objects through API.
        """
        user = User.objects.get(username='testuser')
        self.client.force_authenticate(user=user)
        response = self.client.get('/btms_api/teams/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

        response = self.client.get('/btms_api/teams/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Team A')

    def testGetTeamUnauthorized(self):
        """
        Ensure we can get Team objects through API.
        """
        response = self.client.get('/btms_api/teams/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def testUpdateTeam(self):
        """
        Ensure we can update Team objects through API.
        """
        user = User.objects.get(username='testuser')
        self.client.force_authenticate(user=user)
        team = {'name': 'Team A', 'average_score': 200}
        response = self.client.put('/btms_api/teams/1/', team, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['average_score'], 200)

    def testUpdateTeamUnauthorized(self):
        """
        Ensure we can update Team objects through API.
        """
        team = {'name': 'Team A', 'average_score': 200}
        response = self.client.put('/btms_api/teams/1/', team, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def testDeleteTeam(self):
        """
        Ensure we can delete a Team object through API.
        """
        user = User.objects.get(username='testuser')
        self.client.force_authenticate(user=user)
        response = self.client.delete('/btms_api/teams/1/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class CoachAPITests(APITestCase):

    def setUp(self):
        group = Group(name='admin')
        group.save()
        user = User(first_name='Test', last_name='User', username='testuser', email='test@gmail.com', groups=group)
        user.save()
        team = Team(name='Team A', average_score=145.6)
        team.save()
        coach = Coach(name='Coach A', team=team)
        coach.save()

    def testCreateCoach(self):
        """
        Ensure we can create/post Coach objects through API.
        """
        user = User.objects.get(username='testuser')
        self.client.force_authenticate(user=user)
        coach = {'name': 'Test Team A', 'team': 1}
        response = self.client.post('/btms_api/coaches/', coach, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Coach.objects.count(), 2)

    def testCreateCoachUnauthorized(self):
        """
        Ensure we can create/post Coach objects through API.
        """
        coach = {'name': 'Test Team A', 'team': 1}
        response = self.client.post('/btms_api/coaches/', coach, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def testGetCoach(self):
        """
        Ensure we can get Coach objects through API.
        """
        user = User.objects.get(username='testuser')
        self.client.force_authenticate(user=user)
        response = self.client.get('/btms_api/coaches/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

        response = self.client.get('/btms_api/coaches/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Coach A')

    def testGetCoachUnauthorized(self):
        """
        Ensure we can get Coach objects through API.
        """
        response = self.client.get('/btms_api/coaches/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def testUpdateCoach(self):
        """
        Ensure we can update Coach objects through API.
        """
        user = User.objects.get(username='testuser')
        self.client.force_authenticate(user=user)
        coach = {'name': 'Coach B', 'team': 1}
        response = self.client.put('/btms_api/coaches/1/', coach, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Coach B')


class RoundAPITests(APITestCase):

    def setUp(self):
        group = Group(name='admin')
        group.save()
        user = User(first_name='Test', last_name='User', username='testuser', email='test@gmail.com', groups=group)
        user.save()
        round_obj = Round(round_no=2, round_code='QF', round_name='Quater Final')
        round_obj.save()

    def testCreateRound(self):
        """
        Ensure we can create/post Round objects through API.
        """
        user = User.objects.get(username='testuser')
        self.client.force_authenticate(user=user)
        round_obj = {'round_no': 3, 'round_code': 'SF', 'round_name': 'Semi Final'}
        response = self.client.post('/btms_api/rounds/', round_obj, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Round.objects.count(), 2)

    def testCreateRoundUnauthorized(self):
        """
        Ensure we can create/post Round objects through API.
        """
        round_obj = {'round_no': 3, 'round_code': 'SF', 'round_name': 'Semi Final'}
        response = self.client.post('/btms_api/rounds/', round_obj, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def testGetRound(self):
        """
        Ensure we can get Round objects through API.
        """
        user = User.objects.get(username='testuser')
        self.client.force_authenticate(user=user)
        response = self.client.get('/btms_api/rounds/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response = self.client.get('/btms_api/rounds/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['round_code'], 'QF')

    def testGetRoundUnauthorized(self):
        """
        Ensure we can get Round objects through API.
        """
        response = self.client.get('/btms_api/rounds/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def testUpdateRound(self):
        """
        Ensure we can update Round objects through API.
        """
        user = User.objects.get(username='testuser')
        self.client.force_authenticate(user=user)
        round_obj = {'round_no': 3, 'round_code': 'SF', 'round_name': 'Semi Finals'}
        response = self.client.put('/btms_api/rounds/1/', round_obj, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['round_name'], 'Semi Finals')

    def testDeleteRound(self):
        """
        Ensure we can delete a Round object through API.
        """
        user = User.objects.get(username='testuser')
        self.client.force_authenticate(user=user)
        response = self.client.delete('/btms_api/rounds/1/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class MatchAPITests(APITestCase):

    def setUp(self):
        group = Group(name='admin')
        group.save()
        user = User(first_name='Test', last_name='User', username='testuser', email='test@gmail.com', groups=group)
        user.save()
        round_obj_qf = Round(round_no=1, round_code='QF', round_name='Quater Final')
        round_obj_qf.save()
        round_obj_sf = Round(round_no=2, round_code='SF', round_name='Semi Final')
        round_obj_sf.save()
        team1 = Team(name='Team A', average_score=145.6)
        team2 = Team(name='Team B', average_score=125.1)
        team3 = Team(name='Team C', average_score=145.6)
        team4 = Team(name='Team D', average_score=125.1)
        team1.save()
        team2.save()
        team3.save()
        team4.save()
        match = Match(match_no=1, date='2022-03-01', time='10:00:00', venue='Stadium A', host_team_final_score=120,
                      guest_team_final_score=128, round=round_obj_qf, host_team=team1, guest_team=team2,
                      winner_team=team2)
        match.save()

    def testCreateMatch(self):
        """
        Ensure we can create/post Match objects through API.
        """
        user = User.objects.get(username='testuser')
        self.client.force_authenticate(user=user)
        match = {'match_no': 2, 'date': '2022-03-01', 'time': '10:00:00', 'venue': 'Stadium A',
                 'host_team_final_score': 120,
                 'guest_team_final_score': 128, 'round': 2, 'host_team': 3, 'guest_team': 4, 'winner_team': 3}
        response = self.client.post('/btms_api/matches/', match, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Match.objects.count(), 2)

    def testGetMatch(self):
        """
        Ensure we can get Match objects through API.
        """
        user = User.objects.get(username='testuser')
        self.client.force_authenticate(user=user)
        response = self.client.get('/btms_api/matches/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response = self.client.get('/btms_api/matches/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['winner_team'], 2)

    def testGetMatchUnauthorized(self):
        """
        Ensure we can get Match objects through API.
        """
        response = self.client.get('/btms_api/matches/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def testGetMatchWithRoundFilter(self):
        """
        Ensure we can get Match objects with Round query param through API.
        """
        user = User.objects.get(username='testuser')
        self.client.force_authenticate(user=user)
        match = {'match_no': 2, 'date': '2022-03-01', 'time': '10:00:00', 'venue': 'Stadium A',
                 'host_team_final_score': 120,
                 'guest_team_final_score': 128, 'round': 2, 'host_team': 3, 'guest_team': 4, 'winner_team': 3}
        response = self.client.post('/btms_api/matches/', match, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        response = self.client.get('/btms_api/matches/?round=1')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        for data in response.data:
            self.assertEqual(data['round'], 1)

    def testGetMatchWithRoundFilterWithErrorScenario(self):
        """
        Ensure we can get Match objects with Round query param error scenario through API.
        """
        user = User.objects.get(username='testuser')
        self.client.force_authenticate(user=user)
        match = {'match_no': 2, 'date': '2022-03-01', 'time': '10:00:00', 'venue': 'Stadium A',
                 'host_team_final_score': 120,
                 'guest_team_final_score': 128, 'round': 2, 'host_team': 3, 'guest_team': 4, 'winner_team': 3}
        response = self.client.post('/btms_api/matches/', match, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        response = self.client.get('/btms_api/matches/?round=x')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def testUpdateMatch(self):
        """
        Ensure we can update Match objects through API.
        """
        user = User.objects.get(username='testuser')
        self.client.force_authenticate(user=user)
        match = {'match_no': 2, 'date': '2022-03-01', 'time': '10:00:00', 'venue': 'Stadium A',
                 'host_team_final_score': 125,
                 'guest_team_final_score': 128, 'round': 1, 'host_team': 3, 'guest_team': 4, 'winner_team': 3}
        response = self.client.put('/btms_api/matches/1/', match, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['host_team_final_score'], 125)


class PlayerAPITests(APITestCase):

    def setUp(self):
        group = Group(name='admin')
        group.save()
        user = User(first_name='Test', last_name='User', username='testuser', email='test@gmail.com', groups=group)
        user.save()
        team_1 = Team(name='Team A', average_score=145.6)
        team_2 = Team(name='Team B', average_score=145.6)
        team_1.save()
        team_2.save()
        player = Player(name='Player A', position='Defence', age=27, number_of_games_played=3, penalty_count=2,
                        height=176.80, weight=81.350, average_score=34.9, is_team_captain=True, team=team_1)
        player.save()

    def testCreatePlayer(self):
        """
        Ensure we can create/post Match objects through API.
        """
        user = User.objects.get(username='testuser')
        self.client.force_authenticate(user=user)
        player = {'name': 'Player A', 'position': 'Defence', 'age': 27, 'number_of_games_played': 3,
                  'penalty_count': 2,
                  'height': 176.80, 'weight': 81.350, 'average_score': 34.9, 'is_team_captain': True, 'team': 1}
        response = self.client.post('/btms_api/players/', player, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Player.objects.count(), 2)

    def testGetPlayer(self):
        """
        Ensure we can get Player objects through API.
        """
        user = User.objects.get(username='testuser')
        self.client.force_authenticate(user=user)
        response = self.client.get('/btms_api/players/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response = self.client.get('/btms_api/players/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Player A')

    def testGetPlayerUnauthorized(self):
        """
        Ensure we can get Player objects through API.
        """
        response = self.client.get('/btms_api/players/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def testGetPlayerWithTeamFilter(self):
        """
        Ensure we can get Player objects with team filter through API.
        """
        user = User.objects.get(username='testuser')
        self.client.force_authenticate(user=user)
        player = {'name': 'Player A', 'position': 'Defence', 'age': 27, 'number_of_games_played': 3,
                  'penalty_count': 2,
                  'height': 176.80, 'weight': 81.350, 'average_score': 34.9, 'is_team_captain': True, 'team': 2}
        response = self.client.post('/btms_api/players/', player, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        response = self.client.get('/btms_api/players/?team=1')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        for data in response.data:
            self.assertEqual(data['team'], 1)

    def testGetPlayerWithTeamFilterErrorScenario(self):
        """
        Ensure we can get Player objects with team filter invalid scenario through API.
        """
        user = User.objects.get(username='testuser')
        self.client.force_authenticate(user=user)
        player = {'name': 'Player A', 'position': 'Defence', 'age': 27, 'number_of_games_played': 3,
                  'penalty_count': 2,
                  'height': 176.80, 'weight': 81.350, 'average_score': 34.9, 'is_team_captain': True, 'team': 2}
        response = self.client.post('/btms_api/players/', player, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        response = self.client.get('/btms_api/players/?team=x')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def testGetPlayerWithTeamAndPercentileFilter(self):
        """
        Ensure we can get Player objects with team and percentile query params through API.
        """
        user = User.objects.get(username='testuser')
        self.client.force_authenticate(user=user)
        player = {'name': 'Player A', 'position': 'Defence', 'age': 27, 'number_of_games_played': 3,
                  'penalty_count': 2,
                  'height': 176.80, 'weight': 81.350, 'average_score': 34.9, 'is_team_captain': True, 'team': 2}
        response = self.client.post('/btms_api/players/', player, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        response = self.client.get('/btms_api/players/?team=1&percentile=90')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        for data in response.data:
            self.assertEqual(data['team'], 1)

    def testUpdatePlayer(self):
        """
        Ensure we can update Player objects through API.
        """
        user = User.objects.get(username='testuser')
        self.client.force_authenticate(user=user)
        player = {'name': 'Player A', 'position': 'Attack', 'age': 27, 'number_of_games_played': 3,
                  'penalty_count': 2,
                  'height': 176.80, 'weight': 81.350, 'average_score': 34.9, 'is_team_captain': True, 'team': 1}
        response = self.client.put('/btms_api/players/1/', player, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['position'], 'Attack')


