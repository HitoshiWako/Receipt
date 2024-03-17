from django import forms
from .models import Receipt,Store

class ImageForm(forms.ModelForm):
    class Meta:
        model = Receipt
        fields = ['image']

class ReceiptForm(forms.ModelForm):
    class Meta:
        model = Receipt
        fields = ['date','store']
        widgets = {
            'date': forms.NumberInput(attrs={
                "type": "date"
            })
        }

class StoreForm(forms.ModelForm):
    class Meta:
        model = Store
        fields = ['name','branch']