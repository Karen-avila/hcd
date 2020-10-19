from quda.core.formsBase import *
from .models import *

class ProfilingFileForm(ModelForm):
    class Meta:
        model = ProfilingFile
        fields = '__all__'
