from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _
from .forms import CustomUserChangeForm,CustomUserCreationForm
from .models import User
# Register your models here.


class UserAdmin(BaseUserAdmin):
    ordering = ["email"]
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    list_display = ["pkid","id","email","username","first_name","last_name","is_staff","is_active"]
    list_display_links = ["id","email"]
    list_filter = ["email","username","last_name","first_name","is_staff","is_active"]