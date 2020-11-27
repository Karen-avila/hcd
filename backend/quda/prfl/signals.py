from quda.core.signalsBase import *
from .models import *

post_save.connect(post_save_subscription, sender=Profiling, dispatch_uid="prflprofiling_post_save")
post_delete.connect(post_delete_subscription, sender=Profiling, dispatch_uid="prflprofiling_post_delete")

post_save.connect(post_save_subscription, sender=ProfilingFile, dispatch_uid="prflprofilingfile_post_save")
post_delete.connect(post_delete_subscription, sender=ProfilingFile, dispatch_uid="prflprofilingfile_post_delete")
