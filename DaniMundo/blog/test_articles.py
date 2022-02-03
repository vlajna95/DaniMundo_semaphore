from django.test import TestCase
from blog.models import Article


class ArticleTestCase(TestCase):
	def test_article(self):
		article = Article(title="Test article", summary="Article summary", body="Article body")
		self.assertEqual(article.title, "Test article")
		self.assertEqual(article.summary, "Article summary")
		self.assertEqual(article.body, "Article body")
