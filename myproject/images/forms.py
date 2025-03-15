from django import forms
from .models import UplaodedImage

class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = UplaodedImage
        fields = ('image',)

