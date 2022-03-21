from apps.account.forms.agree_form import AgreeForm
from apps.account.forms.user_creation_form import CustomUserCreationForm
from apps.account.forms.user_modify_form import UserModifyForm
from apps.account.models import MyUser
from django.contrib.auth.models import Group
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from etc.utils import get_first_error_message


def agree(request):
    if request.method == 'GET':
        return render(request, 'account/agree.html')
    elif request.method == 'POST':
        form = AgreeForm(request.POST)
        if form.is_valid():
            return redirect('account:register')
        else:
            return render(request, 'account/agree.html', {'form': form})


def register(request):
    if request.method == 'GET':
        return render(request, 'account/join_form.html')
    elif request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            roles = form.cleaned_data.get('roles')
            account = form.save()
            set_group(account, roles)

            # username = form.cleaned_data.get('username')
            # raw_password = form.cleaned_data.get('password1')
            # user = authenticate(username=username, password=raw_password)  # 사용자 인증
            # login(request, user)  # 로그인
            context = {'redirect': reverse('index:login')}
            return JsonResponse(context)
        else:
            msg = get_first_error_message(form.errors.items())
            context = {'msg': msg}
            return JsonResponse(context, status=401)


def modify(request):
    if request.method == 'GET':
        return render(request, 'account/join_form.html', {'account': request.user})
    elif request.method == 'POST':
        form = UserModifyForm(request.POST, instance=request.user)
        if form.is_valid():
            roles = form.cleaned_data.get('roles')
            account = form.save()
            set_group(account, roles)

            context = {'redirect': reverse('index:login')}
            return JsonResponse(context)
        else:
            msg = get_first_error_message(form.errors.items())
            context = {'msg': msg}
            return JsonResponse(context, status=401)


def set_group(account, roles):
    group_list = []
    for role in roles:
        if role == '1':
            group = Group.objects.get(name='patient')
            group_list.append(group)
        elif role == '2':
            group = Group.objects.get(name='doctor')
            group_list.append(group)
    account.groups.set(group_list)
