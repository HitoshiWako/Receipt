from typing import Any
from django.db.models.query import QuerySet
from django.forms import BaseModelForm
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render,get_object_or_404,redirect
from django.views import generic
from django.urls import reverse_lazy

# Create your views here.
from .forms import ImageForm,ReceiptForm,StoreForm
from .models import Receipt
    
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
        return redirect('index')

def store(request, receipt_id):
    receipt = get_object_or_404(Receipt,pk=receipt_id)
    form = StoreForm()
    params = {
        'title': '店名登録',
        'receipt': receipt,
        'store_form': form
    }
    if request.method == 'POST':
        form = StoreForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('input',receipt.id)
    return render(request, 'receipt/store.html',params)
