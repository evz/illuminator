from django.core.management.base import BaseCommand

from django.core.management import call_command

class Command(BaseCommand):
    args=''
    help=''
    option_list= BaseCommand.option_list + ()

    def get_version(self):
        return "0.1"

    def handle(self, *args, **options):
        call_command('LoadWards')
        call_command('LoadTifDistricts')
        call_command('LoadTifProjReports')
        # call_command('MakeOverlaps')

