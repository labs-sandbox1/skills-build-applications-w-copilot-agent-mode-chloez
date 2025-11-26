from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from djongo import models

from octofit_tracker import models as app_models

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Delete existing data
        app_models.User.objects.all().delete()
        app_models.Team.objects.all().delete()
        app_models.Activity.objects.all().delete()
        app_models.Leaderboard.objects.all().delete()
        app_models.Workout.objects.all().delete()

        # Create Teams
        marvel = app_models.Team.objects.create(name='Team Marvel')
        dc = app_models.Team.objects.create(name='Team DC')

        # Create Users (Superheroes)
        users = [
            app_models.User.objects.create(name='Iron Man', email='ironman@marvel.com', team=marvel),
            app_models.User.objects.create(name='Captain America', email='cap@marvel.com', team=marvel),
            app_models.User.objects.create(name='Spider-Man', email='spiderman@marvel.com', team=marvel),
            app_models.User.objects.create(name='Batman', email='batman@dc.com', team=dc),
            app_models.User.objects.create(name='Superman', email='superman@dc.com', team=dc),
            app_models.User.objects.create(name='Wonder Woman', email='wonderwoman@dc.com', team=dc),
        ]

        # Create Activities
        activities = [
            app_models.Activity.objects.create(user=users[0], type='Run', duration=30, distance=5),
            app_models.Activity.objects.create(user=users[1], type='Swim', duration=45, distance=2),
            app_models.Activity.objects.create(user=users[3], type='Bike', duration=60, distance=20),
        ]

        # Create Workouts
        workouts = [
            app_models.Workout.objects.create(name='Morning Cardio', description='Cardio for all heroes'),
            app_models.Workout.objects.create(name='Strength Training', description='Strength for all heroes'),
        ]

        # Create Leaderboard
        app_models.Leaderboard.objects.create(team=marvel, points=150)
        app_models.Leaderboard.objects.create(team=dc, points=120)

        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data.'))
