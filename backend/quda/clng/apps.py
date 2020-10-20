from quda.core.appsBase import *

class CleaningConfig(AppConfig):
    name = "quda.clng"
    verbose_name = ("LIMPIEZA")
    def ready(self):
        try:
            from .models import CleaningRules
            CleaningRules.initCleaningRules()
        except:
            pass
