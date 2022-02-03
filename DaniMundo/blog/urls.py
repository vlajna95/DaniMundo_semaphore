from django.urls import path
from .views import ArticleListView, ArticleDetailsView, UserDetailsView

urlpatterns = [
	path("", ArticleListView.as_view(), name="article_list"),
	path("<slug:slug>_<int:year>-<int:month>-<int:day>", ArticleDetailsView.as_view(), name="article_details"),
	path("users/<int:pk>", UserDetailsView.as_view(), name="user_details"),
]
