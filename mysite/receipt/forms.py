from django import forms
from .models import Receipt,Store

class ImageForm(forms.ModelForm):
    class Meta:
        model = Receipt
        fields = ['image']

class ReceiptForm(forms.ModelForm):
    class Meta:
        model = Receipt
        fields = ['date','store_id']
        widgets = {
            'date': forms.NumberInput(attrs={
                "type": "date"
            })
        }
        labels ={
            'date':'日付',
            'store_id':'店名'
        }

class StoreForm(forms.ModelForm):
    class Meta:
        model = Store
        fields = ['name','branch']
        labels = {
            'name':'店名',
            'branch':'支店名'
        }