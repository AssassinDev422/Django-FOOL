from django.core.management.base import BaseCommand
from ...tasks import load_cj_feed as load_cj_feed_task


class Command(BaseCommand):
    help = 'Use locally to populate initial data for Podcasts'

    def handle(self, *args, **options):
        load_cj_feed_task()
