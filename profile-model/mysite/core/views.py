from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from .forms import SignUpForm


@login_required
def home(request):
    return render(request, 'home.html')


def signup(request):   
    if request.method == 'POST':
        form = SignUpForm(request.POST,request.FILES)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.profile.birth_date = form.cleaned_data.get('birth_date')
            user.profile.location = form.cleaned_data.get('location')
            user.profile.image = form.cleaned_data.get("image")
            user.profile.bio = form.cleaned_data.get('bio')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})
