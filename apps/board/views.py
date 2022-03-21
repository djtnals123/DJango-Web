from apps.board.decorators import is_writer
from apps.board.forms import BoardForm
from apps.board.models import Board
from django.contrib.auth.decorators import permission_required, login_required
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, resolve_url, redirect
from etc.utils import get_first_error_message


@login_required
@permission_required(perm='board.view_board')
def list(request):
    page = request.GET.get('page', '1')  # 페이지
    per_page = request.GET.get('per_page', '10')  # 페이지당 게시글 수
    option = request.GET.get('option')  # 검색옵션
    keyword = request.GET.get('keyword')  # 검색어

    board_list = Board.objects.order_by('-pk')

    if option and keyword:  # 검색기준
        if option == 'content':  # 내용
            q = Q(content__icontains=keyword)
        elif option == 'title+content':  # 제목+내용
            q = Q(title__icontains=keyword) | \
                Q(content__icontains=keyword)
        elif option == 'writer':  # 작성자
            q = Q(writer__username__icontains=keyword)
        else:  # 제목
            q = Q(title__icontains=keyword)
        board_list = board_list.filter(q).distinct()

    # 페이징처리
    paginator = Paginator(board_list, per_page)
    page_obj = paginator.get_page(page)

    context = {'board_list': page_obj, 'keyword': keyword, 'option': option}
    return render(request, 'board/board_list.html', context)


@login_required
@permission_required(perm='board.view_board')
def read(request, board_id):
    board = get_object_or_404(Board, pk=board_id)
    return render(request, 'board/board_read.html', {'board': board})


@login_required
@permission_required(perm='board.add_board')
def write(request):
    if request.method == 'GET':
        return render(request, 'board/board_write.html')
    if request.method == 'POST':
        form = BoardForm(request.POST, request.FILES)
        if form.is_valid():
            board = form.save(commit=False)
            board.writer = request.user
            board.save()
            context = {'redirect': resolve_url('board:read', board.id)}
            return JsonResponse(context)
        else:
            msg = get_first_error_message(form.errors.items())
            context = {'msg': msg}
            return JsonResponse(context, status=401)


@login_required
@is_writer
@permission_required(perm='board.change_board')
def modify(request, board):
    if request.method == 'GET':
        return render(request, 'board/board_write.html', {'board': board})
    elif request.method == 'POST':
        form = BoardForm(request.POST, request.FILES, instance=board)
        if form.is_valid():
            board = form.save(commit=False)
            board.save()

            context = {'redirect': resolve_url('board:read', board.id)}
            return JsonResponse(context)
        else:
            msg = get_first_error_message(form.errors.items())
            context = {'msg': msg}
            return JsonResponse(context, status=401)


@login_required
@is_writer
@permission_required(perm='board.delete_board')
def delete(request, board):
    board.delete()
    return redirect('board:list')
