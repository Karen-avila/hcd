from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from django.contrib.auth import get_user_model

class BaseAdmin(admin.ModelAdmin):
	pass