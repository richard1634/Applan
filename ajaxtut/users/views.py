from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm


# Create your views here.
def register_view(request, *args, **kwargs):
	if request.method == "POST":
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save();
			username = form.cleaned_data.get('username')
			messages.success(request, f'Account created for {username}. You can login now!')
			return redirect('login')
	else:
		form = UserRegisterForm()	
	return render(request, 'users/register.html', {'form':form})


@login_required
def profile_view(request):
	return render(request,'users/profile.html')