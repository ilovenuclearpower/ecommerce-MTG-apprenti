from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegisterForm

# Create your views here.
def register(request):
    request.user
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()           
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'register/register.html', {'form':form})