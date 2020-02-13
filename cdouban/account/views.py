from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomerForm
from .models import UserAccount
# Create your views here.

def people(request):
	return render(request, 'account/people.html')


def account_login(request):
    if request.method == 'POST':
        user = authenticate(request, username= request.POST['username'], password = request.POST['password'])
        if user is None:
            return render(request, 'account/login.html',{'error':'用户名或密码错误，请重新输入。'})
        else:
            login(request, user)
            return redirect('account:people')
            ## 暂时先返回用户首页
    else:
        return render(request, 'account/login.html')

def account_logout(request):
	logout(request)
	return redirect('account:people')
	#暂时先返回此页

def account_register(request):
	if request.method == 'POST':
		regform = CustomerForm(request.POST)
		if regform.is_valid():
			regform.save()
			login_user = authenticate(username= regform.cleaned_data['username'], password = regform.cleaned_data['password1'])
			login(request, login_user)
			login_user.email = regform.save()
			UserAccount(user_account = login_user, nickname=regform.cleaned_data['nickname'], birthday = regform.cleaned_data['birthday'], \
				location = regform.cleaned_data['location']).save()
			#头像在这步加入会报csrf错误
			return redirect ('account:people')
	else:
		regform = CustomerForm()
		# regform = UserCreationForm()

	content = {'regiserform': regform}
	return render(request, 'account/register.html', content)