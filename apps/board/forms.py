from apps.board.models import Board
from django import forms


class BoardForm(forms.ModelForm):
    class Meta:
        model = Board  # 사용할 모델
        fields = ['title', 'attachment', 'content']
        labels = {
            'title': '제목',
            'attachment': '첨부파일',
            'content': '내용',
        }
