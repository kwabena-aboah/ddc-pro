import datetime
from django.core.management.base import BaseCommand
from record_form.models import PersonInfo


class Command(BaseCommand):
    help = """
		Saves personal information not updated in last 24 hours

		Use this command in a cron job
		to save older records

		you can test if the subcommand works by doing:
		python3 manage.py save_old
		"""

    def handle(self, **options):
        now = datetime.datetime.now()
        yesterday = now - datetime.timedelta(1)
        old_info = PersonInfo.objects.filter(updated_on__lte=yesterday)
        old_info.save()
