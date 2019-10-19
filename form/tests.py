from django.test import TestCase, Client
from django.urls import reverse, resolve
from form.views import contact, feedback
from form.models import FeedbackForm 
from form.forms import FieldForm

# Create your tests here.

class TestUrls(TestCase):
    def test_contact_url_resolves(self):
        url = reverse('form:contact')
        self.assertEquals(resolve(url).func, contact)

    def test_feedback_url_resolves(self):
        url = reverse('form:feedbackform')
        self.assertEquals(resolve(url).func, feedback)

class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.contact = reverse('form:contact')
        self.feedback = reverse('form:feedbackform')

    def test_contact_view_GET(self):
        response = self.client.get(self.contact)
        self.assertTrue(response.status_code==200)
        self.assertTemplateUsed(response, 'contact/index.html')

    def test_feedback_view_GET(self):
        response = self.client.get(self.feedback)
        self.assertTrue(response.status_code==200)
        self.assertTemplateUsed(response, 'feedbackform/index.html')

class TestModels(TestCase):
    def feedback_form_models(self):
        feedback_form = FeedbackForm.objects.save(
            Faculty='FASILKOM',
            Satisfaction='10',
            Comment='Good'
        )
        counting_all_available = FeedbackForm.objects.all().count()
        self.assertEquals(counting_all_available, 1)
    
    def feedback_form_models_success(self):
        response_post = Client().post(reverse('form:feedbackform'),
        {
            'Faculty':'FASILKOM',
            'Satisfaction':'10',
            'Comment':'Good'
        })
        self.assertTrue(response_post.status_code==200)
        
class TestForms(TestCase):
    def test_field_forms_valid(self):
        form = FieldForm(data={
            'Faculty': 'FASILKOM',
            'Satisfaction':'10', 
            'Comment':'Good'
        })
        self.assertTrue(form.is_valid())
        
    def test_field_forms_notValid(self):
        form = FieldForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 3)
        






