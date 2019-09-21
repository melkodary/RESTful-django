from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import ugettext_lazy as _
from django.core.validators import RegexValidator
from .managers import UserManger

# Create your models here.

GENDER_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female'),
    ('O', 'Other'),
)
EGYPT_COUNTRY_CODE = '+20'
US_COUNTRY_CODE = '+1'

COUNTRY_CODE_CHOICES = (
    (EGYPT_COUNTRY_CODE, 'EG'),
    (US_COUNTRY_CODE, 'US'),
)

MY_REGEX = r'^[1-9][0-9]{9,14}$'
TWILO_REGEX = r'^\+[1-9]\d{10,14}$'


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True, null=False)
    first_name = models.CharField(_('first name'), max_length=30, null=True, blank=True)
    last_name = models.CharField(_('last name'), max_length=30, null=True, blank=True)
    birth_date = models.DateField(_('birth date'), null=True, blank=True)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='M')
    phone = models.CharField(max_length=16, unique=True, null=False,
                             validators=[RegexValidator(regex=TWILO_REGEX,
                                                        message="Must be in E.164 i.e +xxxxxxxxxxxxx")])
    is_staff = models.BooleanField(_('staff status'), default=False)
    objects = UserManger()

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = ['email']

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    # def get_phone(self):
    #     return '%s%s' % (self.country_code, self.phone)

    def __str__(self):
        return self.get_full_name()

    def natural_key(self):
        return self.phone

    def get_full_name(self):
        """
        Returns the first_name plus the last_name, with a space in between.
        """
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        """
        Returns the short name for the user.
        """
        return self.first_name
