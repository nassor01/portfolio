from django.test import TestCase, Client
from django.urls import reverse
from .models import Profile, Project, Skill
from .forms import ContactForm

class PortfolioModelTests(TestCase):
    def test_profile_creation(self):
        profile = Profile.objects.create(
            name="Test User",
            role="Developer",
            bio="A test bio",
            email="test@example.com"
        )
        self.assertEqual(str(profile), "Test User")

    def test_project_creation(self):
        project = Project.objects.create(
            title="Test Project",
            description="A test description"
        )
        self.assertEqual(str(project), "Test Project")

    def test_skill_creation(self):
        skill = Skill.objects.create(
            name="Django",
            category="Development"
        )
        self.assertEqual(str(skill), "Development: Django")

class PortfolioViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.profile = Profile.objects.create(
            name="Test User",
            role="Developer",
            bio="A test bio",
            email="test@example.com"
        )

    def test_home_view_status_code(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_home_view_context(self):
        response = self.client.get(reverse('home'))
        self.assertIn('profile', response.context)
        self.assertIn('projects', response.context)
        self.assertIn('skills', response.context)
        self.assertIn('form', response.context)

    def test_home_view_post_valid_form(self):
        data = {
            'name': 'John Doe',
            'email': 'john@example.com',
            'message': 'Hello there!'
        }
        response = self.client.post(reverse('home'), data)
        self.assertEqual(response.status_code, 200) # Form submission rerenders the page with messages
        messages = list(response.context['messages'])
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), "Message transmitted successfully!")

    def test_home_view_post_invalid_form(self):
        data = {
            'name': 'John Doe',
            'email': 'invalid-email',
            'message': ''
        }
        response = self.client.post(reverse('home'), data)
        self.assertEqual(response.status_code, 200)
        messages = list(response.context['messages'])
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), "Error transmitting message. Please check the details.")

class ContactFormTests(TestCase):
    def test_valid_contact_form(self):
        data = {
            'name': 'Alice',
            'email': 'alice@example.com',
            'message': 'Testing the form'
        }
        form = ContactForm(data=data)
        self.assertTrue(form.is_valid())

    def test_invalid_contact_form(self):
        data = {
            'name': '',
            'email': 'not-an-email',
            'message': ''
        }
        form = ContactForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors)
        self.assertIn('message', form.errors)
