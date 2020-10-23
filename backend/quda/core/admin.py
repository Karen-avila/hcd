from quda.core.adminBase import *
from .models import *

@admin.register(Module)
class ModuleAdmin(BaseAdmin):
    pass

@admin.register(Organization)
class OrganizationAdmin(BaseAdmin):
    pass

User = get_user_model()
@admin.register(User)
class UserAdmin(BaseAdmin):
    pass
