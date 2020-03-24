from django.test import TestCase
from .models import Event
from .views import index, getEvent, eventDetail, newEvent
from .forms import EventForm
from django.urls import reverse
from django.contrib.auth.models import User


class EventTest(TestCase):
    def setup(self):
        self.test_user = User.objects.create_user(
            username='newnew', password='what')
        test = Event.objects.create(title='college event', location='seattle central college', date='2020-10-20',
                                    time='12:00:02', description='tech job fair', url='http://www.w3schools.com', userId=self.test_user)
        return test

    def test_string(self):
        test = self.setUp()
        self.assertEqual(str(test.title), 'college event')
        self.assertEqual(str(test.location), 'seattle central college')
        self.assertEqual(str(test.date), '2020-10-20')
        self.assertEqual(str(test.time), '12:00:02')
        self.assertEqual(str(test.description), 'tech job fair')
        self.assertEqual(str(test.url), 'http://www.w3schools.com')
        self.assertEqual(str(test.userId), 'newnew')

    def test_table(self):
        self.assertEqual(str(Event._meta.db_table), 'event')


class Event_Form_Test(TestCase):
    def test_eventform_is_valid(self):
        self.test_user = User.objects.create_user(
            username='newnew', password='what')
        form = EventForm(
            data={'title': "test", 'location': "test server", 'date': "2020-10-20", 'time': "12:00:02", 'description': "seattle", 'url': "http://www.w3schools.com", 'userId': self.test_user})
        self.assertTrue(form.is_valid())

    def test_eventform_empty(self):
        form = EventForm(data={'title': ""})
        self.assertFalse(form.is_valid())


class New_Meeting_authentication_test(TestCase):
    def setUp(self):
        self.test_user = User.objects.create_user(
            username='testuser1', password='P@ssw0rd1')
        self.meeting = Event.objects.create(title='python', location='project', date='2019-04-02',
                                            time='10:20:24', description='scc', url='http://www.w3schools.com', userId=self.test_user)

    def test_redirect_if_not_logged_in(self):
        response = self.client.get(reverse('newEvent'))
        self.assertRedirects(
            response, '/accounts/login/?next=/itBoardApp/newEvent')

    def test_Logged_in_uses_correct_template(self):
        login = self.client.login(username='testuser1', password='P@ssw0rd1')
        response = self.client.get(reverse('newEvent'))
        self.assertEqual(str(response.context['user']), 'testuser1')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'itBoardApp/newEvent.html')
