from __future__ import absolute_import, unicode_literals
from misc.scraper.seismology import scrape_earthquakes
from celery import shared_task

@shared_task
def fetch_earthquake_data():
    scrape_earthquakes()
