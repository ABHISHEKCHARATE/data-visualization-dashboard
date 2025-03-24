import json
from django.core.management.base import BaseCommand
from dashboard.models import DataPoint
from datetime import datetime
from django.utils.timezone import make_aware

class Command(BaseCommand):
    help = 'Load JSON data into the database'

    def handle(self, *args, **kwargs):
        with open('jsondata.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
            for entry in data:
                added_datetime = datetime.strptime(entry['added'], '%B, %d %Y %H:%M:%S')
                added_datetime = make_aware(added_datetime)

                published_datetime = None
                if entry.get('published'):
                    published_datetime = datetime.strptime(entry['published'], '%B, %d %Y %H:%M:%S')
                    published_datetime = make_aware(published_datetime)

                DataPoint.objects.create(
                    end_year=entry.get('end_year', ''),
                    intensity=int(entry.get('intensity', 0) or 0), 
                    sector=entry.get('sector', ''),
                    topic=entry.get('topic', ''),
                    insight=entry.get('insight', ''),
                    url=entry.get('url', ''),
                    region=entry.get('region', ''),
                    start_year=entry.get('start_year', ''),
                    impact=entry.get('impact', ''),
                    added=added_datetime,
                    published=published_datetime,
                    country=entry.get('country', ''),
                    relevance=int(entry.get('relevance', 0) or 0), 
                    pestle=entry.get('pestle', ''),
                    source=entry.get('source', ''),
                    title=entry.get('title', ''),
                    likelihood=int(entry.get('likelihood', 0) or 0),  
                )
        self.stdout.write(self.style.SUCCESS('Successfully loaded data'))
