from quda.core.apps import *

class QudaConfig(AppConfig):
    name = "quda.quda"
    verbose_name = ("QUDA")
    def ready(self):
        try:
            from .models import DataType
            if not DataType.objects.all():
                DataType.objects.create(code="boolean", name="Booleano", isDefault=True)
                DataType.objects.create(code="numerical", name="Numerico", isDefault=True)
                DataType.objects.create(code="date", name="Fecha", isDefault=True)
                DataType.objects.create(code="categorical", name="Texto", isDefault=True)
                DataType.objects.create(code="url", name="Ruta de internet", isDefault=True)
                DataType.objects.create(code="path", name="Ruta de archivo", isDefault=True)
                DataType.objects.create(code="file", name="Archivo", isDefault=True)
                DataType.objects.create(code="image", name="Imagen", isDefault=True)
        except:
            pass

