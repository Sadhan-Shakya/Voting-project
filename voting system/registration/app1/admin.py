from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser,PollOptions,Poll
# from .models import Category, CategoryItem






class CustomUserAdmin(UserAdmin):
    list_display = ('username','first_name', 'last_name', 'email', 'role', 'is_active', 'is_staff', 'is_superuser')

admin.site.register(CustomUser,CustomUserAdmin)


admin.site.register(Poll)
admin.site.register(PollOptions)


# 