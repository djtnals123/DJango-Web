from apps.account.forms.user_creation_form import CustomUserCreationForm
from apps.account.models import MyUser


class UserModifyForm(CustomUserCreationForm):
    class Meta:
        model = MyUser
        fields = ('password1', 'password2', 'email', 'name', 'hospital')