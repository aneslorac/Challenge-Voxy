from django import forms

class CounterForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea(attrs={'cols': 100, 'rows': 10}))