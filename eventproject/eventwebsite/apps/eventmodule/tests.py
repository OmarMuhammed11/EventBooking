from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Event

class EventTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.event = Event.objects.create(title='Test Event', description='This is a test event.', date='2024-04-30', time='12:00:00', location='Test Location', organizer=self.user)

    def test_event_list_view(self):
        response = self.client.get(reverse('event_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.event.title)

    def test_event_detail_view(self):
        response = self.client.get(reverse('event_detail', args=[self.event.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.event.title)

    # Add more test cases as needed.
