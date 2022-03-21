from apps.account.forms.user_creation_form import CustomUserCreationForm
from apps.account.models import MyUser
from django.contrib import admin
# Register your models here.
from django.contrib.auth.admin import UserAdmin
from importlib._common import _


class CustomUserAdmin(UserAdmin):
    model = MyUser
    list_display = ('username', 'email', 'name', 'hospital')
    readonly_fields = ["date_joined", 'last_login']
    form = CustomUserCreationForm
    add_form = CustomUserCreationForm
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('name', 'email', 'hospital')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'email', 'name', 'hospital')}
         ),
    )


admin.site.register(MyUser, CustomUserAdmin)
