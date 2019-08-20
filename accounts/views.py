from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.conf import settings # !!
from django.views.generic import CreateView
from .forms import SignupForm

signup = CreateView.as_view(model=User,
                            success_url=settings.LOGIN_URL,
                            template_name='accounts/signup.html', form_class=UserCreationForm)

'''
def signup(request):
    if request.method == 'POST':
        form = SigunupForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect(settings.LOGIN.URL)
    else:
        form = SigunupForm()
    return render(request, 'accounts/signup.html',{
        'form':form, })
'''

@login_required # 로그아웃 상황일 때 settings.LOGIN_URL로 이동
def profile(request):
    return render(request, 'accounts/profile.html')

