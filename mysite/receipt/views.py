from django.shortcuts import render,get_object_or_404

# Create your views here.
from .forms import UploadForm
from .models import UploadImage

def index(request):
    params = {
        'title': '画像のアップロード',
        'upload_form': UploadForm(),
        'id': None,
        'images':None
    }

    if (request.method == 'POST'):
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            upload_image = form.save()

            params['id'] = upload_image.id
    params['images'] = UploadImage.objects.order_by('-id')

    return render(request, 'receipt/index.html', params)