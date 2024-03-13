from django import forms
from .models import Receipt

class ImageForm(forms.ModelForm):
    class Meta:
        model = Receipt
        fields = ['image']

class ReceiptForm(forms.ModelForm):
    class Meta:
        model = Receipt
        fields = ['date']
        widgets = {
            'date': forms.NumberInput(attrs={
                "type": "date"
            })
        }