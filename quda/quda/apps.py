from quda.core.apps import *

class QudaConfig(AppConfig):
    name = "quda.quda"
    verbose_name = ("QUDA")
    def ready(self):
        try:
            import quda.quda.signals
        except ImportError:
            pass
