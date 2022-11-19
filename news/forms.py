from django import forms
from django.forms import ValidationError
from .models import *

class AddPostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].empty_label = "Категоря не выбрана"
    class Meta:
        model = News
        fields = ['title', 'slug', 'content', 'id_published', 'photo', 'category']
        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control form-control-sm'}),
            'content':forms.Textarea(attrs={'class':'form-control form-control-sm', 'cols':40, 'rows':7}),
            'slug':forms.TextInput(attrs={'class':'form-control form-control-sm'}),
            'id_published':forms.CheckboxInput(attrs={'class':'form-check-input form-check-input-sm'}),
            'category':forms.Select(attrs={'class':'form-select form-select-sm'}),
            'photo':forms.FileInput(attrs={'class':'form-control form-control-sm'})
        }
        
    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) < 3:
            raise ValidationError("Название новости слишком короткое")
        return title
    # title = forms.CharField(max_length=150, label="Заголовок",
    #     widget=forms.TextInput(attrs={'class':'form-control'}))
    # slug = forms.SlugField(max_length=255, 
    #     widget=forms.TextInput(attrs={'class':'form-control'}))
    # content = forms.CharField(widget=forms.Textarea(attrs={'cols':60, 'rows':10, 'class':'form-control'}))
    # id_published = forms.BooleanField(required=False, initial=True, 
    #     widget=forms.CheckboxInput(attrs={'class':'form-check-input'}))
    # category = forms.ModelChoiceField(queryset=Categories.objects.all(), 
    #     empty_label='Категории не выбраны',
    #     widget=forms.Select(attrs={'class':'form-select'}))

    