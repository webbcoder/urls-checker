from django import forms
from .models import UrlsChecker, Link


class UrlsCheckerForms(forms.ModelForm):

    class Meta:
        model = UrlsChecker

        labels = {
            'links': ''
        }
        fields = ['author', 'links']
        widgets = {
            'links': forms.CheckboxSelectMultiple(attrs={
                'class': 'list-unstyled',
            }),
        }


class IntervalForm(forms.ModelForm):

    class Meta:
        model = UrlsChecker
        fields = ['interval']


class LinkForm(forms.ModelForm):

    class Meta:
        model = Link
        fields = ['title', 'url']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'url': forms.URLInput(attrs={'class': 'form-control'})
        }
