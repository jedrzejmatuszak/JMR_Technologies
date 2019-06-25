from django.forms import ModelForm
from shortener.models import URL
from django import forms


class URLForm(ModelForm):
    url = forms.URLField()

    class Meta:
        model = URL
        fields = ['url']
