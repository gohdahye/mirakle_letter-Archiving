

# basic library
from django.contrib import auth, messages
from django.contrib.auth import authenticate
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_protect

# 회원가입 함수
# all_team : team 이름을 보여주기 위한 값 반
from accounts.forms import UserForm


@csrf_protect
def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)

        if form.is_valid():

            id = form.cleaned_data.get('username')
            pw = form.cleaned_data.get('password1')
            form.save()
            user = authenticate(request, username=id, password=pw)
            auth.login(request, user)
            return redirect('/')

    else:
        form = UserForm()

    return render(request, 'accounts/signup.html', {'form': form })


# 로그인 함수
@csrf_protect
def login(request):
    if request.method == "POST":

        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:

            return render(request, 'accounts/login.html', messages.error(request, '아이디 혹은 비밀번호가 잘못되었습니다.'))
    else:
        return render(request, 'accounts/login.html')


# 로그아웃 함수
@csrf_protect
def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('/')
    return render(request, 'single_pages/landing.html')


#회원가입약관
def agreement(request):
    return render(request, 'accounts/agreement.html')