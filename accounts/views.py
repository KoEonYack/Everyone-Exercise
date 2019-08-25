from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.conf import settings
from django.views.generic import CreateView

signup = CreateView.as_view(model=User,
                            success_url=settings.LOGIN_URL,
                            template_name='accounts/signup.html', form_class=UserCreationForm)

@login_required
def profile(request):
    return render(request, 'accounts/profile.html')

