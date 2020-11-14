from quda.core.formsBase import *
from .models import *

class TypeHeaderFileForm(ModelForm):
    class Meta:
        model = TypeHeaderFile
        fields = ('index','headerName')
