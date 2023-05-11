from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

from .models import User, Establishment, Review, Photo

# Register your models here.
class CustomUserAdmin(UserAdmin):
    fieldsets = (
        *UserAdmin.fieldsets,
        (_("Additional Info"), {"fields": ("address", "phone", "age", "_dp")}),
    )

class EstablishmentAdmin(admin.ModelAdmin):
    list_display = ['name', 'rating', 'active']


admin.site.register(User, CustomUserAdmin)
admin.site.register(Establishment, EstablishmentAdmin)
admin.site.register(Review)
admin.site.register(Photo)