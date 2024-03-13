from django.shortcuts import render,get_object_or_404,redirect

# Create your views here.
from .forms import ImageForm,ReceiptForm
from .models import Receipt

def index(request):
    params = {
        'title': '画像のアップロード',
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
    params = {
        'title': 'データ編集',
        'id':receipt_id,
        'receipt_form':ReceiptForm()
    }
    receipt = get_object_or_404(Receipt,pk=receipt_id)
    if (request.method == 'POST'):
        form = ReceiptForm(request.POST,instance=receipt)
        if form.is_valid():
            form.save()
        return redirect('index')
    params['receipt'] = receipt
    return render(request, 'receipt/input.html',params)
