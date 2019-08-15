from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Blog, Post

# from .forms import CustomUserCreationForm, CustomUserChangeForm
# from .models import CustomUser

# class CustomUserAdmin(UserAdmin):
#     add_form = CustomUserCreationForm
#     form = CustomUserChangeForm
#     model = CustomUser
#     list_display = ['email', 'username',]

# admin.site.register(CustomUser, CustomUserAdmin)

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Blog)
admin.site.register(Post)