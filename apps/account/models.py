from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin, Group
)

HOSPITAL_CHOICES = (
    ('S', 'S'),
    ('K', 'K')
)


class UserManager(BaseUserManager):
    def create_user(self, username, password, email, name, hospital, **extra_fields):
        user = self.model(
            username=username,
            password=password,
            email=email,
            name=name,
            hospital=hospital
        )
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password, email):
        user = self.create_user(
            username=username,
            password=password,
            email=email,
            name='admin',
            hospital='S',
        )
        user.is_admin = True
        user.is_superuser = True
        user.is_staff = True

        group1 = Group.objects.get(name='patient')
        group2 = Group.objects.get(name='doctor')
        group_list = [group1, group2]
        user.groups.set(group_list)

        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser, PermissionsMixin):
    class Meta:
        db_table = "user"

        # permissions = (
        #     ("role_doctor", "Role doctor"),
        #     ("role_patient", "Role patient"),
        #     ("role_admin", "Role admin"),
        # )

    username = models.CharField(
        max_length=10,
        unique=True,
        verbose_name="username"
    )
    email = models.EmailField(
        verbose_name='Email address',
        max_length=255,
        unique=True,
    )
    name = models.CharField(
        verbose_name='Name',
        max_length=30,
        unique=False
    )
    hospital = models.CharField(
        verbose_name='Hospital',
        max_length=1,
        unique=False,
        choices=HOSPITAL_CHOICES
    )

    # @property
    # def roles(self):
    #     roles_str = ''
    #     if self.is_staff:
    #         roles_str += '관리자 '
    #     for group in self.groups.all():
    #         roles_str += str(group) + ' '
    #     return roles_str
    #
    # @property
    # def hospital_(self):
    #     if self.hospital == 'S':
    #         return '서울대병원'
    #     elif self.hospital == 'K':
    #         return '고려대병원'

    date_joined = models.DateTimeField(auto_now_add=True, editable=False)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.username
