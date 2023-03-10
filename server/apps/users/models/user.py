from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.users.db.managers import CustomUserManager

from server.apps.core.db.mixins import Timestamps


class User(Timestamps, AbstractBaseUser, PermissionsMixin):
    login = models.CharField(
        max_length=150,
        null=True,
        blank=True,
        unique=True,
        verbose_name=_('VN__LOGIN'),
        help_text=_('HT__LOGIN')
    )

    email = models.EmailField(
        max_length=150,
        null=True,
        blank=True,
        unique=True,
        verbose_name=_('VN__EMAIL'),
        help_text=_('HT__EMAIL')
    )

    is_staff = models.BooleanField(
        default=True,
        verbose_name=_('VN__IS_STAFF'),
        help_text=_('HT__IS_STAFF')
    )

    is_active = models.BooleanField(
        default=True,
        verbose_name=_('VN__IS_ACTIVE'),
        help_text=_('HT__IS_ACTIVE')
    )

    reset_password_hash = models.CharField(
        max_length=150,
        null=True,
        blank=True,
        unique=True,
        verbose_name=_('VN__RESET_PASSWORD_HASH'),
        help_text=_('HT__RESET_PASSWORD_HASH')
    )

    USERNAME_FIELD = 'login'

    objects = CustomUserManager()

    class Meta:
        verbose_name = _('VN__USER')
        verbose_name_plural = _('VN__USERS')
        ordering = ('login',)

    def __str__(self):
        return self.login

    def get_short_name(self):
        return self.login
