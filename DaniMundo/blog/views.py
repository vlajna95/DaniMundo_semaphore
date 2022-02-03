from django.views.generic import ListView, DetailView
from .models import CustomUser, Article


class ArticleListView(ListView):
	model = Article
	template_name = "blog/article_list.html"


class ArticleDetailsView(DetailView):
	model = Article
	template_name = "blog/article_details.html"


class UserDetailsView(DetailView):
	model = CustomUser
	template_name = "blog/user_details.html"
