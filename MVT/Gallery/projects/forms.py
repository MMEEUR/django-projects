from django import forms
from .models import Project
from django.utils.text import slugify
from urllib import request
from django.core.files.base import ContentFile

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['rating']
    '''  
    def clean_url(self):
        url = self.changed_data['url']
        valid_extensions = ['jpg', 'jpeg', 'png']
        extension = url.rsplit('.', 1)[1].lower()
        if extension not in valid_extensions:
            raise forms.ValidationError('The extension is not valid(only |jpg|jpeg|png| files')
        
        return url
    
    def save(self, force_insert=False, force_update=False, commit=True):
        image = super().save(commit=False)
        image_url = self.cleaned_data['url']
        name = slugify(image.title)
        extension = image_url.rsplit('.', 1)[1].lower()
        image_name = f'{name}.{extension}'
        response = request.urlopen(image_url)
        image.image.save(image_name, ContentFile(response.read()), save=False)
        
        if commit:
            image.save()
        
        return image
    '''