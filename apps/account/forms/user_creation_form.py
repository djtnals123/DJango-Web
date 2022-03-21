from apps.account.models import MyUser
from importlib._common import _

from django import forms
from django.contrib.auth.forms import UserCreationForm


ROLE_CHOICES = (
    ('1', 'PATIENT'),
    ('2', 'DOCTOR')
)


class CustomUserCreationForm(UserCreationForm):
    roles = forms.MultipleChoiceField(label='roles', choices=ROLE_CHOICES, error_messages={'required': '회원형태를 선택해 주세요.'})

    class Meta:
        model = MyUser
        fields = ('username', 'password1', 'password2', 'email', 'name', 'hospital')
        error_messages = {
            'username': {
                'required': '아이디를 입력해주세요.',
            }
        }
