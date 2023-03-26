# forms.py

from django import forms

class LocationForm(forms.Form):
    location = forms.ChoiceField(choices=[('Delhi', 'Delhi'), ('Maharashtra', 'Maharashtra'), ('kerala', 'Kerala')])
