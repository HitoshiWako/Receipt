from django.shortcuts import render,get_object_or_404,redirect

# Create your views here.
from .forms import ImageForm,ReceiptForm,StoreForm
from .models import Receipt

def index(request):
    params = {
        'title': 'レシート一覧',
        'image_form': ImageForm(),
        'id': None,
    }

    if (request.method == 'POST'):
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            receipt = form.save()
            params['id'] = receipt.id
    params['receipts'] = Receipt.objects.order_by('-id')

    return render(request, 'receipt/index.html', params)

def input(request, receipt_id):
    receipt = get_object_or_404(Receipt,pk=receipt_id)
    form = ReceiptForm(instance=receipt)
    params = {
        'title': 'データ編集',
        'receipt':receipt,
        'receipt_form':form
    }
    if (request.method == 'POST'):
        form = ReceiptForm(request.POST,instance=receipt)
        if form.is_valid():
            form.save()
        return redirect('index')
    return render(request, 'receipt/input.html',params)

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
