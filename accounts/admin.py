from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin
# from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import User

# class CustomUserAdmin(UserAdmin):
#     add_form = CustomUserCreationForm
#     form = CustomUserChangeForm
#     model = User
#     ordering = ('is_staff',)
#     list_filter = ()
#     list_display = ['email', 'first_name', 'last_name', 'avatar', 'birth_date', 'phone', 'gender', 'is_staff']


class UserAdmin(admin.ModelAdmin):
    list_display = ['email', 'is_staff']


admin.site.register(User, UserAdmin)
# admin.site.register(User, CustomUserAdmin)
