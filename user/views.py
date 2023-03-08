from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserSigninForm

def signup(request):
    if request.method == 'POST':
        form = UserSigninForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('blog-index')
    else:
        form = UserSigninForm()
    context = {
        'form': form
    }
    return render(request, 'user/signup.html', context)
