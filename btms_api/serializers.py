from rest_framework import serializers
from .models import Team, Coach, Player, Round, Match, User


class TeamSerializer(serializers.ModelSerializer):

    class Meta:
        model = Team
        fields = '__all__'


class CoachSerializer(serializers.ModelSerializer):

    class Meta:
        model = Coach
        fields = ['name', 'team']


class PlayerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Player
        fields = '__all__'


class RoundSerializer(serializers.ModelSerializer):

    class Meta:
        model = Round
        fields = '__all__'


class MatchSerializer(serializers.ModelSerializer):

    class Meta:
        model = Match
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'first_name', 'last_name', 'username', 'password', 'groups', 'email')
        model = User
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        user.set_password(validated_data['password'])
        user.is_staff = True
        user.save()

        return user
