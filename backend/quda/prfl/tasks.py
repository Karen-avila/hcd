from celery import shared_task
from django.apps import apps

@shared_task
def makeProfiling(profilingFile):
    profilingfile = apps.get_model('prfl', 'ProfilingFile').objects.get(id=profilingFile)
    profilingfile.makeProfiling()
    return 'Perfilamiento {0} terminado'.format(profilingfile.id)
