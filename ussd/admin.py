from django.contrib import admin
from .models import UserSession, Account

# Register your models here.
class UserSessionAdmin(admin.ModelAdmin):
    list_display = ("session_id", "phone_number", "step")

class AccountAdmin(admin.ModelAdmin):
    list_display = ("phone_number", "balance", "account_number")

# Register each model separately with its admin class
admin.site.register(UserSession, UserSessionAdmin)
admin.site.register(Account, AccountAdmin)
