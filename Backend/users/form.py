from django.forms import ModelForm
from .models import TempImage
from cloudinary.forms import CloudinaryFileField
from django import forms

class TempImageForm(ModelForm):
    file = forms.FileField()

    class Meta:
        model = TempImage
        fields = '__all__'
        