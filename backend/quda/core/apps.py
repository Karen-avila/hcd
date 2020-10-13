from .appsBase import *

class CoreConfig(AppConfig):
    name = "quda.core"
    verbose_name = ("CORE")
    def ready(self):
        try:
            from .models import Organization
            from django.conf import settings
            def defineFirstOrganization():
                if not Organization.objects.filter(code=settings.ORGANIZATION).first():
                    Organization.objects.get_or_create(code=settings.ORGANIZATION, name=settings.ORGANIZATION)
            defineFirstOrganization()
        except Exception as e:
            pass
        try:
            import quda.core.signals
        except ImportError:
            pass
