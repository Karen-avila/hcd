from .appsBase import *

class CoreConfig(AppConfig):
    name = "quda.core"
    verbose_name = ("CORE")
    def ready(self):
        try:
            from .models import Organization, User
            from django.conf import settings
            if settings.DEBUG:
                def defineFirstOrganization():
                    if not Organization.objects.filter(code=settings.ORGANIZATION).first():
                        Organization.objects.create(code=settings.ORGANIZATION, name=settings.ORGANIZATION)
                def createFirstUser():
                    if not User.objects.filter(organization__code=settings.ORGANIZATION).first():
                        organization = Organization.objects.filter(code=settings.ORGANIZATION).first()
                        user = User.objects.create(
                            username=settings.ORGANIZATION + '__admin',
                            organization=organization,
                            is_superuser=True,
                            is_staff=True
                        )
                        user.set_password('admin')
                        user.save()
                defineFirstOrganization()
                createFirstUser()
        except Exception as e:
            pass
        try:
            import quda.core.signals
        except ImportError:
            pass
