from django.contrib.auth.base_user import BaseUserManager


class UserManger(BaseUserManager):
    # use_in_migrations = True

    def get_by_natural_key(self, username):
        print(username)
        return self.get(email=username)

    def _create_user(self, email, password, **extra_fields):

        if not email:
            raise ValueError('email cannot be empty.')

        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        password = password if password is not None else self.make_random_password()

        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)