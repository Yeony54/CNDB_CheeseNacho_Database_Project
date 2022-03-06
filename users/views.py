from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from users.forms import UserForm
from .forms import UpdateForm
from django.contrib.auth.hashers import check_password
from django.contrib import messages, auth
# from django.views.decorators.csrf import csrf_exempt

from users.models import Mlike, Slike, Ugenres
from entmt_info.models import Movies, Series
from django.db.models import Q


# csrf token의 다른 방법
# @csrf_exempt


# 회원가입
def signup(request):
    # POST 방식의 request일 경우
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')

            # 입력받은 username, password로 로그인하기
            user = authenticate(username=username, password=raw_password)
            login(request, user)

            # 회원가입 후 로그인 상태로 메인 페이지 돌아가기
            return redirect('home')
    else:
        form = UserForm()
    return render(request, 'users/signup.html', {'form': form})


def mypage(request):
    user_id = request.user.id
    mlike_list = Mlike.objects.filter(ml_member=user_id)
    mlike_code_list = []
    movie_list = []
    print(mlike_list)
    print('-------------------')
    for mlike in mlike_list:
        # mlike_code_list.append(mlike.ml_movie_id)
        movie_list.append(Movies.objects.get(movie_id=mlike.ml_movie_id))
        # print(f'--{mlike}({mlike.ml_movie_id})={movie_list}')

    # 객체체

   # -------------안됌
    # User_a = request.user
    # movies = User_a.mlike_set.movies_set.all()
    # print(movies)

    print('-------------------')
    print(movie_list)
    content = {
        'movie_list': movie_list
    }
    return render(request, 'users/mypage.html', content)


def change_password(request):
    if request.method == "POST":
        user = request.user
        origin_password = request.POST["origin_password"]
        if check_password(origin_password, user.password):
            new_password = request.POST["new_password"]
            confirm_password = request.POST["confirm_password"]
            if new_password == confirm_password:
                user.set_password(new_password)
                user.save()
                auth.login(request, user, backend='django.contrib.auth.backends.ModelBackend')
                messages.success(request, '비밀번호가 변경되었습니다!')
                return redirect('users:change_password')
            else:
                messages.error(request, '비밀번호가 다릅니다!')
        else:
            messages.error(request, '비밀번호를 잘못 입력하셨습니다.')
        return render(request, 'users/change_password.html')
    else:
        return render(request, 'users/change_password.html')


def update(request):
    if request.method == 'POST':
        update_form = UpdateForm(request.POST,
                                 request.FILES, instance=request.user)

        if update_form.is_valid():
            update_form.save()
            messages.success(request, '회원정보가 변경되었습니다!')
            return redirect('users:update')

    else:
        # user_update_form = UserUpdateForm(instance=request.user)
        update_form = UpdateForm(instance=request.user)

    context = {
        'update_form': update_form
    }
    return render(request, 'users/update.html', context)
