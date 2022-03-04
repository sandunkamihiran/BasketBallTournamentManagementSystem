# Generated by Django 4.0.3 on 2022-03-02 17:12

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Round',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('round_no', models.IntegerField()),
                ('round_code', models.CharField(max_length=10)),
                ('round_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('average_score', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('position', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
                ('number_of_games_played', models.IntegerField()),
                ('penalty_count', models.IntegerField()),
                ('height', models.DecimalField(decimal_places=2, max_digits=10)),
                ('weight', models.DecimalField(decimal_places=3, max_digits=10)),
                ('average_score', models.FloatField()),
                ('is_team_captain', models.BooleanField()),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='btms_api.team')),
            ],
        ),
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('match_no', models.IntegerField()),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('venue', models.CharField(max_length=50)),
                ('host_team_final_score', models.IntegerField()),
                ('guest_team_final_score', models.IntegerField()),
                ('guest_team', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='guest_team', to='btms_api.team')),
                ('host_team', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='host_team', to='btms_api.team')),
                ('round', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='btms_api.round')),
                ('winner_team', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='winner_team', to='btms_api.team')),
            ],
        ),
        migrations.CreateModel(
            name='Coach',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='btms_api.team')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('email', models.EmailField(max_length=50, unique=True)),
                ('groups', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.group')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
