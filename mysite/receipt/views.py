from typing import Any
from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.views import generic
from django.urls import reverse_lazy
from django import forms

# Create your views here.
from .forms import ImageForm,ReceiptForm,StoreForm
from .models import Receipt,Item
    
class IndexView(generic.FormView):
    template_name = 'receipt/index.html'
    form_class = ImageForm
    success_url = reverse_lazy('index')
    extra_context={
        'title':'レシート一覧',
        }
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        ctx = super().get_context_data(**kwargs)
        ctx['receipts']=Receipt.objects.order_by('-id')
        return ctx

    def form_valid(self, form: Any) -> HttpResponse:
        form.save()
        return super().form_valid(form)

class ReceiptView(generic.UpdateView):
    template_name = 'receipt/edit.html'
    form_class = ReceiptForm
    model = Receipt
    ItemFormSet = forms.inlineformset_factory(parent_model=Receipt,model=Item,fields=['name','price','discount','qty'],extra=3)
    success_url = reverse_lazy('index')
    extra_context={
        'title':'データ編集',
        }

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        receipt = Receipt.objects.get(pk = self.kwargs['pk'])
        queryset = Item.objects.filter(receipt_id = receipt)
        ctx = super().get_context_data(**kwargs)
        item_formset = self.ItemFormSet(self.request.POST or None,instance=self.object,queryset=queryset)
        ctx['item_formset']=item_formset
        return ctx
    
    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        ctx = self.get_context_data()
        item_formset = ctx['item_formset']
        if item_formset.is_valid():
            item_formset.save()
        return super().form_valid(form)

class StoreView(generic.CreateView):
    template_name = 'receipt/store.html'
    form_class = StoreForm
    extra_context={
        'title':'店舗登録',
        }
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        ctx = super().get_context_data(**kwargs)
        receipt = get_object_or_404(Receipt,pk=self.kwargs['pk'])
        ctx['receipt'] = receipt
        return ctx
    
    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        newstore = form.save()
        receipt = get_object_or_404(Receipt,pk=self.kwargs['pk'])
        receipt.store_id = newstore
        receipt.save()
        return super().form_valid(form)
    
    def get_success_url(self) -> str:
        return reverse_lazy('edit',kwargs=self.kwargs)