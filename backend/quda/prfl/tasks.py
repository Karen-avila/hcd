from celery import shared_task
from django.apps import apps

@shared_task
def makeProfiling(profilingFile):
    apps.get_model('prfl', 'ProfilingFile').objects.get(id=profilingFile).makeProfiling()
    return 'Perfilamiento {0} terminado'.format(profilingfile.id)
