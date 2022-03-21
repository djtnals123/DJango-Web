import functools

from apps.board.models import Board
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, resolve_url


def is_writer(view):
    @functools.wraps(view)
    def wrapped_view(*args, **kwargs):
        request = args[0]
        board = get_object_or_404(Board, pk=kwargs.get('board_id'))
        if request.method == 'GET':
            if board.writer == request.user:
                return view(request, board)
            else:
                return redirect('board:read', board.id)
        elif request.method == 'POST':
            if board.writer == request.user:
                return view(request, board)
            else:
                context = {'redirect': resolve_url('board:read', board.id)}
                return JsonResponse(context)

    return wrapped_view
