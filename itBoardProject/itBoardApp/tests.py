from django.test import TestCase
from .models import Job
from django.contrib.auth.models import User
from django.urls import reverse

from .views import index, getjobs, getjobsdetails
from .forms import JobForm
# Create your tests here.

# TESTING models
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




#TESTING VIEWS
class IndexTest(TestCase):
   def test_view_url_accessible_by_name(self):
       response = self.client.get(reverse('index'))
       self.assertEqual(response.status_code, 200)
  
class getjobs_test(TestCase):
   def test_view_url_accessible_by_name(self):
       response = self.client.get(reverse('jobs'))
       self.assertEqual(response.status_code, 200)


#TESTING FORMS
class Job_Form_Test(TestCase):
    def test_job_form_is_valid(self):
        form=JobForm(data={'JobTitle': "Digital Product Manager",
        'Employer' : "Starbucks",
        'JobURL' : "https://g.co/kgs/y6fk5g",
        'User' : "John",
        'JobLevel' : "Experienced",
        'Location' : "Seattle, WA",
        'Availability' : "April 1, 2020",
        'Description' : "Job Summary and Mission At Starbucks, our mission is to inspire and nurture the human spirit – one person, one cup, and one neighborhood at a time." })
        self.assertTrue(form.is_valid())

    def test_job_form_is_empty(self):
        form=JobForm(data={'JobTitle': ""})
        self.assertFalse(form.is_valid())




# TESTING Authentication
class New_Job_authentication_test(TestCase):
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

    def test_redirect_if_not_logged_in(self):
        response=self.client.get(reverse('newjob'))
        self.assertRedirects(response, '/accounts/login/?next=/itBoardApp/newjob/')

    def test_Logged_in_uses_correct_template(self):
        self.login=self.client.login(username='testuser1', password='P@ssw0rd1')
        response=self.client.get(reverse('newjob'))
        self.assertEqual(str(response.context['user']), 'testuser1')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'itBoardApp/newjob.html')