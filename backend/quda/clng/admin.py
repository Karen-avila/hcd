from quda.core.adminBase import *
from .models import *

@admin.register(Cleaning)
class CleaningAdmin(BaseAdmin):
    pass

@admin.register(CleaningFile)
class CleaningFileAdmin(BaseAdmin):
    pass

@admin.register(CleaningFileOrderedRulesInColumns)
class CleaningFileOrderedRulesInColumnsAdmin(BaseAdmin):
    pass

@admin.register(CleaningFileColumn)
class CleaningFileColumnAdmin(BaseAdmin):
    pass
