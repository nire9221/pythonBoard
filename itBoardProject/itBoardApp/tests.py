from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Article, Genre
from .forms import ArticleForm
from .views import getarticle, getarticledetail, newArticle

#==================
# Testing Models
#==================
class ArticleTest(TestCase):
    def setUp(self):
        test=Article(articletitle='ABC', articledescription='descriptiondescription', articleurl='http://articlearticle', articledate='2020-03-25')
        return test 
    def test_string(self):
        test=self.setUp()
        self.assertEqual(str(test.articletitle), 'ABC')
        self.assertEqual(str(test.articledescription), 'descriptiondescription')
        self.assertEqual(str(test.articleurl), 'http://articlearticle')
        self.assertEqual(str(test.articledate), '2020-03-25')
    
    def test_table(self):
        self.assertEqual(str(Article._meta.db_table), 'article')

# ==================
# Testing Views
# ==================
class IndexTest(TestCase):
   def test_view_url_accessible_by_name(self):
       response = self.client.get(reverse('index'))
       self.assertEqual(response.status_code, 302)
  
class GetArticleTest(TestCase):
   def test_view_url_accessible_by_name(self):
       response = self.client.get(reverse('article'))
       self.assertEqual(response.status_code, 302)

# ==================
# Testing Forms
# ==================
class Article_Form_Test(TestCase):
    def test_articleform_is_valid(self):
        self.test_user=User.objects.create_user(username='testuser1', password='P@ssw0rd1')
        self.test_genre=Genre.objects.create(genrename='IT')
        form=ArticleForm(data={'articletitle': "testarticle", 'articledescription': "testdescription", 'articleurl': "http://testurl", 'articlegenre': self.test_genre, 'articleuser': self.test_user, 'articledate': "2020-02-12"})
        self.assertTrue(form.is_valid())

    def test_typeform_empty(self):
        form=ArticleForm(data={'articletitle': ""})
        self.assertFalse(form.is_valid())

# ==================
# Testing Authentication
# ==================
class Authentication_test(TestCase):
    def setUp(self):
        self.test_user=User.objects.create_user(username='testuser1', password='P@ssw0rd1')
        self.test_genre=Genre.objects.create(genrename='IT')
        self.article=Article.objects.create(articletitle='ABC', articledescription='descriptiondescription', articleurl='http://articlearticle', articlegenre=self.test_genre, articleuser=self.test_user, articledate='2020-03-25')
        return 
    def test_redirect_if_not_logged_in(self):
        response=self.client.get(reverse('newarticle'))
        self.assertRedirects(response, '/accounts/login/?next=/itBoardApp/newArticle/')

    def test_Logged_in_uses_correct_template(self):
        login=self.client.login(username='testuser1', password='P@ssw0rd1')
        response=self.client.get(reverse('newarticle'))
        self.assertEqual(str(response.context['user']), 'testuser1')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'itBoardApp/newArticle.html')