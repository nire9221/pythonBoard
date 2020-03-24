from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Article, Genre, Event, Job
from .forms import ArticleForm, EventForm, JobForm
from .views import getarticle, getarticledetail, newArticle, getEvent, eventDetail, newEvent, getjobs, getjobsdetails

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

class EventTest(TestCase):
    def setup(self):
        test = Event.objects.create(title='college event', location='seattle central college', date='2020-10-20', time='12:00:02', description='tech job fair', url='http://www.w3schools.com')
        return test

    def test_string(self):
        test = self.setUp()
        self.assertEqual(str(test.title), 'college event')
        self.assertEqual(str(test.location), 'seattle central college')
        self.assertEqual(str(test.date), '2020-10-20')
        self.assertEqual(str(test.time), '12:00:02')
        self.assertEqual(str(test.description), 'tech job fair')
        self.assertEqual(str(test.url), 'http://www.w3schools.com')

    def test_table(self):
        self.assertEqual(str(Event._meta.db_table), 'event')
        
class JobTest(TestCase):
   def test_string_job(self):
       type=Job(JobTitle="Digital Technology Intern")
       self.assertEqual(str(type), type.JobTitle)

   def test_table_job(self):
       self.assertEqual(str(Job._meta.db_table), 'Job')

   def setUp(self):
       user=User.objects.create(username="John", password="bananajeremy")
       self.job=Job(JobTitle="Digital Technology Intern",
       Employer="GE",
       JobURL="https://g.co/kgs/fF53iF",
       User=user,
       JobLevel="Internship",
       Location="Redmond, WA",
       Availability="2020-04-01",
       Description="Interns will learn from the best in the industry and work on substantial projects with real world implications, getting hands-on with digital technologies."
       )

   def test_job_name(self):
       self.assertEqual(str(self.job), self.job.JobTitle)

   def test_job_employer(self):
       self.assertEqual(self.job.Employer, "GE")

   def test_job_url(self):
       self.assertEqual(self.job.JobURL, "https://g.co/kgs/fF53iF")

   def test_job_user(self):
       self.assertTrue(User)

   def test_job_joblevel(self):
       self.assertEqual(self.job.JobLevel, "Internship")

   def test_job_location(self):
       self.assertEqual(self.job.Location, "Redmond, WA")

   def test_job_availability(self):
       self.assertEqual(self.job.Availability, "2020-04-01")

   def test_job_description(self):
       self.assertEqual(self.job.Description, "Interns will learn from the best in the industry and work on substantial projects with real world implications, getting hands-on with digital technologies.")


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

class IndexTest(TestCase):
   def test_view_url_accessible_by_name(self):
       response = self.client.get(reverse('index'))
       self.assertEqual(response.status_code, 302)
  
class getjobs_test(TestCase):
   def test_view_url_accessible_by_name(self):
       response = self.client.get(reverse('jobs'))
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

class Event_Form_Test(TestCase):
    def test_eventform_is_valid(self):
        self.test_user = User.objects.create_user(username='newnew', password='what')
        form = EventForm(
            data={'title': "test", 'location': "test server", 'date': "2020-10-20", 'time': "12:00:02", 'description': "seattle", 'url': "http://www.w3schools.com", 'userId': self.test_user})
        self.assertTrue(form.is_valid())

    def test_eventform_empty(self):
        form = EventForm(data={'title': ""})
        self.assertFalse(form.is_valid())
class Job_Form_Test(TestCase):
    def test_job_form_is_valid(self):
        self.test_user = User.objects.create_user(username='newnew', password='what')
        form=JobForm(data={'JobTitle': "Digital Product Manager",
        'Employer' : "Starbucks",
        'JobURL' : "https://g.co/kgs/y6fk5g",
        'User' : self.test_user,
        'JobLevel' : "Experienced",
        'Location' : "Seattle, WA",
        'Availability' : "2020-03-23",
        'Description' : "Job Summary and Mission At Starbucks, our mission is to inspire and nurture the human spirit one person, one cup, and one neighborhood at a time." })
        self.assertTrue(form.is_valid())

    def test_job_form_is_empty(self):
        form=JobForm(data={'JobTitle': ""})
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

class New_Job_authentication_test(TestCase):
    def setUp(self):
       self.test_user=User.objects.create_user(username='John', password='bananajeremy')
       self.job=Job.objects.create(JobTitle="Digital Technology Intern",
       Employer="GE",
       JobURL="https://g.co/kgs/fF53iF",
       User=self.test_user,
       JobLevel="Internship",
       Location="Redmond, WA",
       Availability="2020-04-01",
       Description="Interns will learn from the best in the industry and work on substantial projects with real world implications, getting hands-on with digital technologies."
       )
       return

    def test_redirect_if_not_logged_in(self):
        response=self.client.get(reverse('newjob'))
        self.assertRedirects(response, '/accounts/login/?next=/itBoardApp/newjob/')

    def test_Logged_in_uses_correct_template(self):
        login=self.client.login(username='testuser1', password='P@ssw0rd1')
        response=self.client.get(reverse('newjob'))
        self.assertEqual(str(response.context['user']), 'testuser1')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'itBoardApp/newjob.html')