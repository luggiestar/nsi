from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.http import HttpResponse
from import_export.admin import ImportExportModelAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import *

# from .resources import AcademicRegistrationResource
# from .resources import *

User = get_user_model()


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    list_display = ('username', 'email', 'first_name', 'middle_name', 'last_name', 'phone', 'sex', 'title', 'is_active',
                    'is_superuser', 'is_staff', 'is_active',)
    list_filter = ('username', 'is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('username', 'password', 'email')}),
        ('personal', {'fields': ('first_name', 'middle_name', 'last_name', 'sex', 'phone', 'title'),
                      }),

        ('Permissions', {'fields': ('is_superuser', 'is_staff', 'is_active', 'groups',
                                    'user_permissions')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'is_staff', 'is_active')}
         ),
    )
    search_fields = ('username',)
    ordering = ('username',)


admin.site.register(User, CustomUserAdmin)
admin.site.register(Category)
admin.site.register(Type)
admin.site.register(Content)
admin.site.register(Programme)
admin.site.register(AboutUs)