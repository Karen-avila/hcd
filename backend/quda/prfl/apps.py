from quda.core.appsBase import *

class ProfilingConfig(AppConfig):
    name = "quda.prfl"
    verbose_name = ("PERFILAMIENTO")
    def ready(self):
        try:
            import quda.prfl.signals
        except ImportError:
            pass
