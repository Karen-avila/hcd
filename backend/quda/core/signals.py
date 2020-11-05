from .signalsBase import *

from .models import *

post_save.connect(post_save_subscription, sender=Organization, dispatch_uid="coreorganization_post_save")
post_delete.connect(post_delete_subscription, sender=Organization, dispatch_uid="coreorganization_post_delete")

