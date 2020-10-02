from .appsBase import *

class CoreConfig(AppConfig):
    name = "quda.core"
    verbose_name = ("CORE")
    def ready(self):
        try:
            import quda.core.signals
        except ImportError:
            pass
