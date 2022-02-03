from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser, Article


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
	model = CustomUser
	add_form = CustomUserCreationForm
	form = CustomUserChangeForm
	# prepopulated_fields = {"slug": ("username", )}
	list_display = ["first_name", "last_name", "username", "email", "date_joined", "last_login"]
	list_filter = ["date_joined", "last_login"]
	search_fields = ["first_name", "last_name", "username", "email"]


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
	prepopulated_fields = {"slug": ("title", )}
	list_display = ["title", "summary", "status", "date_created", "date_updated"]
	list_filter = ["author", "status", "date_created", "date_updated"]
	search_fields = ["title", "summary", "body"]
