from django.test import TestCase
from django.urls import reverse
from .models import About
from .forms import CollaborateForm


class TestAboutViews(TestCase):
    
    def setUp(self):
        """Creates about me content"""
        self.about_content = About(
            title="About Me", content="This is about me.")
        self.about_content.save()
    
    def test_render_about_page_with_collaborate_form(self):
        """Verifies get request for about me containing a collaboration form"""
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'About Me', response.content)
        self.assertIsInstance(
            response.context['collaborate_form'], CollaborateForm)

    def test_successfull_submission_of_collaborate_form(self):
        post_data = {
            'name': 'Manny',
            'email': 'manny@test.com',
            'message': 'hi manny'
        }
        response = self.client.post(reverse('about'), post_data)
        self.assertEqual(response.status_code, 200)
        self.assertIn(
            b'Collaboration request received! I endeavour to respond within 2 working days.',
            response.content
        )