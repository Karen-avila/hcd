from quda.core.adminBase import *
from .models import *

@admin.register(File)
class FileAdmin(BaseAdmin):
    pass

@admin.register(DataType)
class DataTypeAdmin(BaseAdmin):
    pass

@admin.register(TypeHeaderFile)
class TypeHeaderFileAdmin(BaseAdmin):
    pass
