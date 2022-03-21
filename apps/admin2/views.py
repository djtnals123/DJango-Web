from apps.account.models import MyUser
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render


@login_required
@staff_member_required
def user_list(request):
    page = request.GET.get('page', '1')  # 페이지
    per_page = request.GET.get('per_page', '10')  # 페이지당 게시글 수
    account_list = MyUser.objects.order_by('-pk')

    # 페이징처리
    paginator = Paginator(account_list, per_page)
    page_obj = paginator.get_page(page)

    context = {'account_list': page_obj}
    return render(request, 'admin/user_list.html', context)