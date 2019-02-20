from django.core.management.base import BaseCommand
from misc.scraper.seismology import scrape_earthquakes


class Command(BaseCommand):
    help = 'Scrape the data from National Seismological Center'

    def handle(self, **options):
        scrape_earthquakes()
