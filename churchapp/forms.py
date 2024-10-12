from django import forms
from .models import Administration,NewsModel,GalleryModel,EnquiryModel,BlogModel,MassesModel


class Administration_Form(forms.ModelForm):
    class Meta:
        model = Administration
        fields = '__all__'
        
class NewsForm(forms.ModelForm):
    class Meta:
        model = NewsModel
        fields = '__all__'
        
        
class GalleryForm(forms.ModelForm):
    class Meta:
        model = GalleryModel
        fields = '__all__'
        
class EnquiryForm(forms.ModelForm):
    class Meta:
        model = EnquiryModel
        fields = '__all__'
        
class MassForm(forms.ModelForm):
    class Meta:
        model = MassesModel
        fields = '__all__'
        
class BlogForm(forms.ModelForm):
    class Meta:
        model = BlogModel
        fields = '__all__'