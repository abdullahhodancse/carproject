from django.shortcuts import render, redirect
from . import forms

# Create your views here.
def brand(request):
    if request.method == 'POST':
        form = forms.BrandForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('brand')
    else:
        form = forms.BrandForm()
    return render(request, 'brands.html', {'form': form})
