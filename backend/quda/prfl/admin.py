from quda.core.adminBase import *
from .models import *

@admin.register(ProfilingRules)
class ProfilingRulesAdmin(BaseAdmin):
    pass

@admin.register(Profiling)
class ProfilingAdmin(BaseAdmin):
    pass

@admin.register(ProfilingFile)
class ProfilingFileAdmin(BaseAdmin):
    pass

@admin.register(ProfilingFileColumn)
class ProfilingFileColumnAdmin(BaseAdmin):
    readonly_fields = [
        'blanks',
        'ints',
        'floats',
        'dates',
        'strings',
    ]
