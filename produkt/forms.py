from django import forms
from produkt.models import *

class SubscriberForms(forms.ModelForm):
    
    class Meta:
        model = Subscribers
        exclude = [""] 