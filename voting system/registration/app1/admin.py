from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from .models import Profile
from .models import Category, CategoryItem

from .models import UserModel

admin.site.register(UserModel)

class UserModel(UserAdmin):
    list_display=['username','email','role','password']
admin.site.register(CustomUser,UserModel)

admin.site.register(Profile)


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',)}

admin.site.register(Category, CategoryAdmin)
admin.site.register(CategoryItem)



# 