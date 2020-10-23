from quda.core.adminBase import *
from .models import *

@admin.register(Profiling)
class ProfilingAdmin(BaseAdmin):
    pass

@admin.register(ProfilingFile)
class ProfilingFileAdmin(BaseAdmin):
    pass

