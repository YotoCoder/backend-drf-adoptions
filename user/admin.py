from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

# Register your models here.

# admin.site.register(User, UserAdmin)

# modificar el admin de django para que muestre los campos que queremos
@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'is_active')
    list_filter = ('username', 'email','first_name', 'last_name', 'is_staff', 'is_active')
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'phone','password1', 'password2', 'is_staff', 'is_active', 'is_superuser'),
        }),
    )
    search_fields = ('email', 'username')
    ordering = ('email',)