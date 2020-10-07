from .adminBase import *

from .forms import *
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

#class UserAdmin(auth_admin.UserAdmin):
    #form = UserChangeForm
    #add_form = UserCreationForm
    #fieldsets = (("User", {"fields": ("name",)}),) + auth_admin.UserAdmin.fieldsets
    #list_display = ["username", "is_superuser"]

