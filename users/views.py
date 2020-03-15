from django.shortcuts import render,redirect
from .forms import UserRegisterForm,ProfileForm
from django.contrib import messages


def register(request):
    if request.method=='POST':
        form =UserRegisterForm(request.POST)
        pform = ProfileForm(request.POST)

        if form.is_valid() and pform.is_valid():
            user = form.save()
            profile = pform.save(commit=False)
            profile.user = user
            profile.save()
            username=form.cleaned_data.get('username')
            messages.success(request, f'Your account has been successfully created, you\'re now able to log in !')
            return redirect('login')
        else:
             messages.error(request, 'Please correct the errors below')



    form = UserRegisterForm()
    pform = ProfileForm()
    return render(request, 'users/register.html', {'form': form,'pform':pform})
