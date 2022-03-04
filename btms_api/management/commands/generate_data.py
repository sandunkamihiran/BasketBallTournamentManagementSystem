from django.core.management.base import BaseCommand, CommandError
from faker import Faker
from btms_api.models import Team, Round, Coach, Player, Match
import random


class Command(BaseCommand):
    help = 'Generate Dummy Data'

    def create_teams(self, fake):

        for t in range(16):
            try:
                team = Team(name=fake.slug(), average_score=round(random.uniform(100, 200), 2))
                team.save()
            except Exception:
                raise CommandError('Error creating team data')

    def create_rounds(self):

        try:
            round_of_sixteen = Round(round_no=1, round_code='R16', round_name='Round of Sixteen')
            round_qf = Round(round_no=2, round_code='QF', round_name='Quater Finals')
            round_sf = Round(round_no=3, round_code='SF', round_name='Semi Finals')
            round_gf = Round(round_no=4, round_code='GF', round_name='Grand Final')
            round_of_sixteen.save()
            round_qf.save()
            round_sf.save()
            round_gf.save()
        except Exception:
            raise CommandError('Error creating Round data')

    def create_coaches(self, fake):
        teams = Team.objects.all()

        try:
            for team in teams:
                coach = Coach(name=fake.name(), team=team)
                coach.save()
        except Exception:
            raise CommandError('Error creating Coach data')

    def create_players(self, fake):
        teams = Team.objects.all()
        try:
            for team in teams:
                for t in range(10):
                    player = Player(name=fake.name(), position=fake.slug(), age=random.randint(10, 80),
                                    number_of_games_played=random.randint(0, 4), penalty_count=random.randint(0, 4),
                                    height=round(random.uniform(50, 300), 2), weight=round(random.uniform(15, 200), 2),
                                    average_score=round(random.uniform(100, 200), 2), is_team_captain=False, team=team)
                    player.save()

        except Exception:
            raise CommandError('Error creating Player data')

    def create_matches(self, fake):
        #  round 1 matches
        teams = Team.objects.all()
        rounds = Round.objects.all()
        round_one_winners = []
        for t in range(8):
            match = Match(match_no=random.randint(1, 100), date=fake.date(), time=fake.time(),
                          venue=fake.city(), round=rounds[0],
                          host_team=teams[(t * 2)], guest_team=teams[(t * 2 + 1)], winner_team=teams[(t * 2 + 1)],
                          host_team_final_score=round(random.uniform(100, 200), 2),
                          guest_team_final_score=round(random.uniform(100, 200), 2))
            match.save()
            round_one_winners.append(teams[(t * 2 + 1)])

        round_two_winners = []
        for t in range(4):
            match = Match(match_no=random.randint(1, 100), date=fake.date(), time=fake.time(),
                          venue=fake.city(), round=rounds[1],
                          host_team=round_one_winners[(t * 2)], guest_team=round_one_winners[(t * 2 + 1)],
                          winner_team=round_one_winners[(t * 2 + 1)],
                          host_team_final_score=round(random.uniform(100, 200), 2),
                          guest_team_final_score=round(random.uniform(100, 200), 2))
            match.save()
            round_two_winners.append(round_one_winners[(t * 2 + 1)])

        round_three_winners = []
        for t in range(2):
            match = Match(match_no=random.randint(1, 100), date=fake.date(), time=fake.time(),
                          venue=fake.city(), round=rounds[2],
                          host_team=round_two_winners[(t * 2)], guest_team=round_two_winners[(t * 2 + 1)],
                          winner_team=round_two_winners[(t * 2 + 1)],
                          host_team_final_score=round(random.uniform(100, 200), 2),
                          guest_team_final_score=round(random.uniform(100, 200), 2))
            match.save()
            round_three_winners.append(round_two_winners[(t * 2 + 1)])

        for t in range(1):
            match = Match(match_no=random.randint(1, 100), date=fake.date(), time=fake.time(),
                          venue=fake.city(), round=rounds[3],
                          host_team=round_three_winners[(t * 2)], guest_team=round_three_winners[(t * 2 + 1)],
                          winner_team=round_three_winners[(t * 2 + 1)],
                          host_team_final_score=round(random.uniform(100, 200), 2),
                          guest_team_final_score=round(random.uniform(100, 200), 2))
            match.save()

    def handle(self, *args, **kwargs):
        fake = Faker()

        # Generates list of teams
        self.create_teams(fake)

        # Generates list of rounds
        self.create_rounds()

        # Generate list of coaches
        self.create_coaches(fake)

        # Generate list of players
        self.create_players(fake)

        # Generate list of matches
        self.create_matches(fake)
