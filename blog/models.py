from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
# from django.utils.text import slugify
from django.utils.timezone import now
from django.utils.translation import gettext_lazy as _
# from django_lifecycle import LifeCycleModelMixin, hook, AFTER_CREATE, AFTER_UPDATE


class ModelHelper:
	def meta(self):
		return self._meta


class CustomUser(AbstractUser, ModelHelper): #, LifeCycleModelMixin):
	first_name = models.CharField(max_length=50, blank=False, verbose_name=_("first name"))
	last_name = models.CharField(max_length=50, blank=False, verbose_name=_("last name"))
	username = models.CharField(max_length=100, unique=True, verbose_name=_("username"))
	email = models.CharField(max_length=50, blank=False, verbose_name=_("email"))
	slug = models.SlugField(null=True, blank=True, unique=True, verbose_name=_("slug"))

	class Meta:
		verbose_name = _("user")
		verbose_name_plural = _("users")

	def __str__(self):
		return self.get_full_name()

	def get_absolute_url(self):
		return reverse("user_details", args=[self.pk])


class Article(models.Model, ModelHelper): #, LifeCycleModelMixin):
	PUBLICATION_STATUS_CHOICES = [
		("PUBLIC", _("public")),
		("PRIVATE", _("private")),
		("DRAFT", _("draft")),
	]
	title = models.CharField(max_length=200, verbose_name=_("title"))
	summary = models.CharField(max_length=500, verbose_name=_("summary"), help_text=_("The summary of the article (max. 500 characters)"))
	body = models.TextField(verbose_name=_("body"), help_text=_("The body/contents of the article"))
	author = models.ManyToManyField(CustomUser, related_name="articles", verbose_name=_("author(s)"))
	status = models.CharField(choices=PUBLICATION_STATUS_CHOICES, max_length=10, verbose_name=_("article publication status"))
	date_created = models.DateTimeField(default=now, verbose_name=_("date created"))
	date_updated = models.DateTimeField(default=now, verbose_name=_("date updated"))
	slug = models.SlugField(unique=True, verbose_name=_("slug"))

	class Meta:
		verbose_name = _("article")
		verbose_name_plural = _("articles")

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse("article_details", kwargs={"slug": self.slug, "year": self.date_created.year, "month": self.date_created.month, "day": self.date_created.day})
