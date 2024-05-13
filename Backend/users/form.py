from django.forms import ModelForm
from .models import TempImage
from cloudinary.forms import CloudinaryFileField
    
class TempImageForm(ModelForm):
    image = CloudinaryFileField()

    class Meta:
        model = TempImage
        fields = '__all__'