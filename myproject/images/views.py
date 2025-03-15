from django.shortcuts import render, redirect
from .forms import ImageUploadForm
from .models import UplaodedImage
from sorl.thumbnail import get_thumbnail


# Create your views here.

def upload_image(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('image_list')
    else:
        form = ImageUploadForm()
        return render(request, 'images/upload.html', {'form': form})
    
def image_list(request):
    images = UplaodedImage.objects.all()
    return render(request, 'images/list.html', {'images': images})
