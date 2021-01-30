from django.shortcuts import render,redirect
from .form import ContactForm

def home(request):
    if request.method == 'POST':
        f = ContactForm(request.POST)
        if f.is_valid():
            f.save()
            return redirect('index')
    else:
        f = ContactForm()
    return render(request, 'work/home.html', {'form': f})