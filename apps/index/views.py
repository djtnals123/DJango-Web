from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect


def index(request):
    print(request.user.is_authenticated)
    if request.user.is_authenticated:
        return redirect('index:choose_function')
    else:
        return redirect('index:login')


@login_required
def choose_function(request):
    return render(request, 'choose_function_form.html')


