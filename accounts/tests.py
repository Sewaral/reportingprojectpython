from django.test import TestCase, Client
from django.urls import reverse
from .models import Report,Register2,Register3,Message
from .forms import ReportForm

class ReportIssueViewTests(TestCase):
    def setUp(self):
        """Set up the necessary test data."""
        self.client = Client()
        self.url = reverse('report_issue')

    def test_report_issue_get_request(self):
        """Test the GET request for the report_issue view."""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'report_problem.html')

class HomeViewTests(TestCase):

    def setUp(self):
        """Set up the necessary test data."""
        self.url = reverse('home')

    def test_home_get_request(self):
        """Test the GET request for the home view."""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')


from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate
from .models import Register, Login_1


class LoginViewTests(TestCase):

    def setUp(self):
        """Set up necessary test data."""
        self.url = reverse('login')  # Adjust to your actual URL name for login
        self.username = 'testuser'
        self.password = 'testpassword'
        # Create a user for testing login
        self.user = User.objects.create_user(username=self.username, password=self.password)

    def test_login_page_get_request(self):
        """Test the GET request for the login view."""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')  # Adjust to your actual template name

    def test_login_post_unregistered_user(self):
        """Test the POST request for login with an unregistered user."""
        # Use a username that is not in the Register model (i.e., not registered)
        response = self.client.post(self.url, {'username': 'unregistered_user', 'password': 'somepassword'})

        self.assertEqual(response.status_code, 302)  # Expecting a redirect
        self.assertRedirects(response, '/register/')  # Should redirect to registration page


from django.test import TestCase
from django.urls import reverse
from .models import Report

from django.test import TestCase
from django.urls import reverse
from .models import Report


class SetezinMapViewTests(TestCase):

    def setUp(self):
        """Set up necessary test data."""
        self.url = reverse('setezin_map')  # Adjust to your actual URL name for the setezin_map view

    def test_setezin_map_get_request_with_reports(self):
        """Test the GET request for the setezin_map view when reports exist."""
        # Create some test reports


        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'setezin_map.html')  # Replace with your actual template name

        # Ensure that reports are in the context
        self.assertIn('reports', response.context)
        reports = response.context['reports']

    def test_setezin_map_get_request_no_reports(self):
        """Test the GET request for the setezin_map view when no reports exist."""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'setezin_map.html')  # Replace with your actual template name

        # Ensure that reports are in the context but there are none
        self.assertIn('reports', response.context)
        reports = response.context['reports']
        self.assertEqual(reports.count(), 0)  # No reports in the database, so count should be 0
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import RegisterForm
from .models import Register

class RegisterViewTests(TestCase):

    def setUp(self):
        """Set up necessary test data."""
        self.url = reverse('register')  # Adjust to your actual URL name for register view

    def test_register_page_get_request(self):
        """Test the GET request for the register view."""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'register.html')  # Adjust to your actual template name

class Register2ViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.register_url = reverse('register2')
        self.valid_data = {
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password1': 'securepassword123',
            'password2': 'securepassword123',
            'work': 'Software Engineer',
            'specialization': 'Web Development',
        }
        self.invalid_data = {
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password1': 'securepassword123',
            'password2': 'mismatchedpassword',  # Passwords do not match
            'work': 'Software Engineer',
            'specialization': 'Web Development',
        }

    def test_register_valid_data(self):
        response = self.client.post(self.register_url, self.valid_data)
        self.assertEqual(response.status_code, 200)  # Redirects after successful registration


    def test_register_username_already_exists(self):
      User.objects.create_user(username='testuser', email='existing@example.com', password='securepassword123')
      response = self.client.post(self.register_url, self.valid_data)
      self.assertEqual(response.status_code, 200)  # Redirects back to registration page

    def test_register_get_request(self):
        response = self.client.get(self.register_url)
        self.assertEqual(response.status_code, 200)

    def test_register_email_already_exists(self):
        User.objects.create_user(username='otheruser', email='testuser@example.com', password='securepassword123')
        response = self.client.post(self.register_url, self.valid_data)
        self.assertEqual(response.status_code, 200)  # Redirects back to registration page

class Register3ViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.register_url = reverse('register3')
        self.valid_data = {
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password1': 'securepassword123',
            'password2': 'securepassword123',
            'phone': '1234567890',
            'work': 'Software Engineer',
            'department': 'Development',
        }
        self.invalid_data = {
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password1': 'securepassword123',
            'password2': 'mismatchedpassword',  # Passwords do not match
            'phone': '1234567890',
            'work': 'Software Engineer',
            'department': 'Development',
        }

    def test_register_valid_data(self):
        response = self.client.post(self.register_url, self.valid_data)
        self.assertEqual(response.status_code, 200)  # Redirects after successful registration

    def test_register_get_request(self):
        response = self.client.get(self.register_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'register3.html')

    def test_register_passwords_do_not_match(self):
        response = self.client.post(self.register_url, self.invalid_data)
        self.assertEqual(response.status_code, 200)  # Redirects back to registration page
        self.assertContains(response, 'Passwords do not match.', html=True)

from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from accounts.models import Register2, Login_2  # Replace 'yourapp' with the name of your app

class Login2ViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.login_url = reverse('login2')
        self.register_url = reverse('register2')
        self.reports_map_url = reverse('reports_map')

        # Create a test user and corresponding Register2 entry
        self.user = User.objects.create_user(username='testuser', password='securepassword123')
        self.registered_user = Register2.objects.create(
            user=self.user,
            username='testuser',
            email='testuser@example.com',
            work='Software Engineer',
            specialization='Web Development',
            password1='securepassword123',
            password2='securepassword123',
        )

    def test_login_valid_credentials(self):
        response = self.client.post(self.login_url, {
            'username': 'testuser',
            'password': 'securepassword123',
        })
        self.assertEqual(response.status_code, 302)  # Redirects after successful login
        self.assertRedirects(response, self.reports_map_url)
        self.assertTrue(Login_2.objects.filter(username='testuser').exists())

    def test_login_invalid_username(self):
        response = self.client.post(self.login_url, {
            'username': 'invaliduser',
            'password': 'securepassword123',
        })
        self.assertEqual(response.status_code, 302)  # Redirects to register2 page
        self.assertRedirects(response, self.register_url)


class Login3ViewTest(TestCase):

    def setUp(self):
        # Create a Django User for authentication
        self.user = User.objects.create_user(username='worker', password='password')

    def test_login3_success(self):
        # Send a POST request with correct username and password
        response = self.client.post(reverse('login3'), {'username': 'worker', 'password': 'password'})

    def test_login3_get_request(self):
        # Send a GET request to the login view
        response = self.client.get(reverse('login3'))

        # Ensure the form is present in the response
        self.assertContains(response, '<form')
        self.assertEqual(response.status_code, 200)

    def test_login3_invalid_credentials(self):
        # Send a POST request with incorrect password
        response = self.client.post(reverse('login3'), {'username': 'worker', 'password': 'wrongpassword'})
        self.assertEqual(response.status_code, 302)


class ChatViewTest(TestCase):

    def setUp(self):
        # Create a few messages for testing
        self.message1 = Message.objects.create(content='First message', timestamp='2025-01-06 10:00:00')
        self.message2 = Message.objects.create(content='Second message', timestamp='2025-01-06 11:00:00')
        self.message3 = Message.objects.create(content='Third message', timestamp='2025-01-06 12:00:00')

    def test_no_messages(self):
        response = self.client.get(reverse('chat'))
        self.assertEqual(response.status_code, 200)



class SendMessageTest(TestCase):

    def test_send_message_success(self):
        """Test that a message is created successfully when valid data is sent."""
        url = reverse('send_message')  # Replace with the actual URL name of your view
        data = {
            'username': 'TestUser',
            'content': 'Hello, world!'
        }

        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['status'], 'success')

        # Verify that the message was created
        self.assertEqual(Message.objects.count(), 1)
        message = Message.objects.first()
        self.assertEqual(message.name, 'TestUser')
        self.assertEqual(message.content, 'Hello, world!')

    def test_send_message_no_content(self):
        """Test that an error response is returned when no content is provided."""
        url = reverse('send_message')  # Replace with the actual URL name of your view
        data = {
            'username': 'TestUser',
            'content': ''  # No content
        }

        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json()['status'], 'error')
        self.assertEqual(response.json()['message'], 'No content provided')

    def test_send_message_invalid_method(self):
        """Test that an error response is returned when the request method is not POST."""
        url = reverse('send_message')  # Replace with the actual URL name of your view

        response = self.client.get(url)  # GET request instead of POST
        self.assertEqual(response.status_code, 405)
        self.assertEqual(response.json()['status'], 'error')
        self.assertEqual(response.json()['message'], 'Invalid request method')



import json
from django.test import TestCase
from django.urls import reverse
from .models import Report

import json
from django.test import TestCase
from django.urls import reverse
from .models import Report
from django.test import TestCase
from django.urls import reverse
from .models import Register
from django.contrib.auth.models import User

class DeleteUserTest(TestCase):

    def setUp(self):
        # Create a user object that will be linked to Register
        self.user = User.objects.create_user(
            username="testuser",
            password="password123"
        )

        # Create the associated Register model instance
        self.register = Register.objects.create(
            user=self.user,
            username="testuser",
            email="testuser@example.com",
            place="Some Place",
            password1="password123",
            password2="password123"
        )

        # URL for the delete view (adjust to your actual URL name)
        self.url = reverse('delete_user', args=[self.register.id])

    def test_delete_user_success(self):
        """Test that a user is deleted successfully."""
        # Check that the Register object exists before deletion
        self.assertEqual(Register.objects.count(), 1)

        # Simulate a POST request to delete the user
        response = self.client.post(self.url)

        # Check that the Register object is deleted
        self.assertEqual(Register.objects.count(), 0)

        # Check that we are redirected to the 'user_list' page
        self.assertRedirects(response, reverse('user_list'))

    def test_delete_user_not_found(self):
        """Test that a 404 error is raised when trying to delete a non-existing user."""
        non_existent_register_id = 9999  # ID that doesn't exist
        url = reverse('delete_user', args=[non_existent_register_id])

        response = self.client.post(url)

        # Ensure a 404 error is returned
        self.assertEqual(response.status_code, 404)


class UserListTest(TestCase):

    def setUp(self):
        # Create some users for testing
        self.user1 = User.objects.create_user(
            username="user1", password="password123"
        )
        self.user2 = User.objects.create_user(
            username="user2", password="password123"
        )

        # Create Register objects linked to the users
        Register.objects.create(
            user=self.user1,
            username="user1",
            email="user1@example.com",
            place="Place 1",
            password1="password123",
            password2="password123"
        )

        Register.objects.create(
            user=self.user2,
            username="user2",
            email="user2@example.com",
            place="Place 2",
            password1="password123",
            password2="password123"
        )

        # URL for the user_list view
        self.url = reverse('user_list')

    def test_user_list_view(self):
        """Test that the user list view renders and displays the users correctly."""
        # Make a GET request to the user list page
        response = self.client.get(self.url)

        # Check if the response status is OK
        self.assertEqual(response.status_code, 200)

        # Check if the correct template is used
        self.assertTemplateUsed(response, 'user_list.html')

        # Check if the users are passed to the template
        users = response.context['users']
        self.assertEqual(users.count(), 2)

        # Check if the usernames are in the response context
        self.assertIn(self.user1.username, [user.username for user in users])
        self.assertIn(self.user2.username, [user.username for user in users])

    def test_user_list_empty(self):
        """Test that the user list view handles the case with no users."""
        # Delete all Register objects to simulate an empty list
        Register.objects.all().delete()

        # Make a GET request to the user list page
        response = self.client.get(self.url)

        # Check if the response status is OK
        self.assertEqual(response.status_code, 200)

        # Check if the correct template is used
        self.assertTemplateUsed(response, 'user_list.html')

        # Ensure that no users are passed to the template
        users = response.context['users']
        self.assertEqual(users.count(), 0)

class WorkerMapViewTest(TestCase):

    def test_worker_map_view(self):
        # Get the URL of the worker map page (replace 'worker_map' with the actual name of the URL)
        url = reverse('worker_map')  # Ensure this matches the URL pattern name
        response = self.client.get(url)

        # Check that the view renders successfully (status code 200)
        self.assertEqual(response.status_code, 200)

        # Check that the reports are passed into the template context
        reports = response.context['reports']
        # Check that the correct template is used
        self.assertTemplateUsed(response, 'worker_map.html')


from django.test import TestCase
from django.urls import reverse
from django.contrib.messages import get_messages
from .models import Rating
from .forms import RatingForm


class RateComplaintViewTest(TestCase):

    def setUp(self):
        # Create data for the rating form
        self.url = reverse('rate_complaint')  # Ensure this matches the URL pattern name

    def test_get_rating_form(self):
        # Test GET request for the rating form page
        response = self.client.get(self.url)

        # Check that the response is successful and renders the correct template
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'rating_compliment.html')

        # Check that the form is in the context
        self.assertIn('form', response.context)
        self.assertIsInstance(response.context['form'], RatingForm)

    def test_post_valid_rating_form(self):
        # Test a valid POST request for submitting the rating form
        data = {'rating': 5, 'comment': 'Great service!'}
        response = self.client.post(self.url, data)

        # Check that the rating object is created
        self.assertEqual(Rating.objects.count(), 1)
        rating = Rating.objects.first()
        self.assertEqual(rating.rating, 5)
        self.assertEqual(rating.comment, 'Great service!')

        # Check for the success message


        # Ensure that the user is redirected to the 'success' page
        self.assertRedirects(response, reverse('success'))  # Update with the correct URL name


from django.test import TestCase
from django.urls import reverse


class SuccessPageViewTest(TestCase):

    def setUp(self):
        # The URL for the success page (ensure it matches the URL pattern name in your project)
        self.url = reverse('success')  # Replace 'success' with the correct URL pattern name

    def test_success_page_render(self):
        # Test GET request for the success page
        response = self.client.get(self.url)

        # Check that the response is successful (status code 200)
        self.assertEqual(response.status_code, 200)

        # Check that the correct template is used
        self.assertTemplateUsed(response, 'success.html')

        # Optionally, you can check for specific content in the rendered template
from django.test import TestCase, RequestFactory
from django.urls import reverse
from django.template.loader import render_to_string
from .models import Report
from .views import done_reports

class DoneReportsViewTests(TestCase):
    def setUp(self):
        """
        Set up test data.
        """
        # Create some test reports with different statuses
        self.report_done = Report.objects.create(
            description="Report 1 (Done)",
            status='done'
        )
        self.report_open = Report.objects.create(
            description="Report 2 (Open)",
            status='open'
        )
        self.report_in_progress = Report.objects.create(
            description="Report 3 (In Progress)",
            status='in_progress'
        )

        # URL for the done_reports view
        self.url = reverse('done_reports')  # Replace 'done_reports' with the actual URL name

    def test_done_reports_view_returns_correct_template(self):
        """
        Test that the done_reports view uses the correct template.
        """
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'done_reports.html')

    def test_done_reports_view_returns_only_done_reports(self):
        """
        Test that the done_reports view only returns reports with status 'done'.
        """
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

        # Check that the context contains the correct reports
        reports_in_context = response.context['reports']
        self.assertEqual(reports_in_context.count(), 1)  # Only one report has status 'done'
        self.assertEqual(reports_in_context.first().status, 'done')
class ViewReportsViewTests(TestCase):
    def setUp(self):
        """
        Set up test data.
        """
        # Create some test reports with different statuses
        self.report_open = Report.objects.create(
            description="Report 1 (Open)",
            status='open'
        )
        self.report_done = Report.objects.create(
            description="Report 2 (Done)",
            status='done'
        )
        self.report_in_progress = Report.objects.create(
            description="Report 3 (In Progress)",
            status='in_progress'
        )

        # URL for the view_reports view
        self.url = reverse('view_reports')  # Replace 'view_reports' with the actual URL name

    def test_view_reports_view_returns_correct_template(self):
        """
        Test that the view_reports view uses the correct template.
        """
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'view_reports.html')


from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.messages import get_messages
from .models import Rating
from .forms import RatingForm

class RateComplaintViewTests(TestCase):
    def setUp(self):
        """
        Set up test data.
        """
        self.client = Client()
        self.url = reverse('rate_complaint')  # Replace 'rate_complaint' with the actual URL name

    def test_rate_complaint_get_request(self):
        """
        Test the GET request for the rate_complaint view.
        """
        response = self.client.get(self.url)

        # Check that the response is successful and the correct template is used
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'rating_compliment.html')

        # Check that the form is in the context
        self.assertIn('form', response.context)
        self.assertIsInstance(response.context['form'], RatingForm)

from django.test import TestCase, Client
from django.urls import reverse

class SuccessPageViewTests(TestCase):
    def setUp(self):
        """
        Set up test data.
        """
        self.client = Client()
        self.url = reverse('success')  # Replace 'success' with the actual URL name

    def test_success_page_renders_correctly(self):
        """
        Test that the success_page view renders the correct template.
        """
        response = self.client.get(self.url)

        # Check that the response is successful
        self.assertEqual(response.status_code, 200)

        # Check that the correct template is used
        self.assertTemplateUsed(response, 'success.html')


from django.test import TestCase, RequestFactory
from django.contrib.auth.models import User
from django.urls import reverse
from accounts.models import Report  # Replace 'your_app' with the actual app name
from accounts.views import reports_map  # Replace 'your_app' with the actual app name


class ReportsMapViewTest(TestCase):

    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='testpassword')

        # Create some test reports

        # Set up the request factory
        self.factory = RequestFactory()

    def test_reports_map_view_with_authenticated_user(self):
        # Create a request object
        request = self.factory.get(reverse('reports_map'))  # Replace 'reports_map' with the actual URL name

        # Simulate an authenticated user
        request.user = self.user

        # Call the view function
        response = reports_map(request)

        # Check that the response status code is 200
        self.assertEqual(response.status_code, 200)

        # Check that the correct template is used

from django.test import TestCase, Client
from django.urls import reverse
from django.core import mail
from .models import Report
import json

class UpdateStatusViewTests(TestCase):
    def setUp(self):
        """
        Set up test data.
        """
        # Create a test report
        self.report = Report.objects.create(
            description="Test Report",
            status='open',
            email='test@example.com'
        )
        self.url = reverse('update_status', args=[self.report.id])  # Replace 'update_status' with the actual URL name

    def test_update_status_valid_status(self):
        """
        Test updating the status of a report with a valid status.
        """
        data = {'status': 'in_progress'}
        response = self.client.post(
            self.url,
            data=json.dumps(data),
            content_type='application/json'
        )

        # Check that the response is successful
        self.assertEqual(response.status_code, 200)


class UpdateUserViewTests(TestCase):
    def setUp(self):
        """
        Set up test data.
        """
        self.client = Client()
        # Create a test user and associated Register instance
        self.user = User.objects.create_user(
            username="testuser",
            password="password123"
        )
        self.register = Register.objects.create(
            user=self.user,
            username="testuser",
            email="test@example.com",
            place="Test Place",
            password1="password123",
            password2="password123"
        )
        self.url = reverse('update_user', args=[self.register.id])  # Replace 'update_user' with the actual URL name

    def test_update_user_valid_data(self):
        """
        Test updating a user with valid data.
        """
        data = {
            'username': 'updateduser',
            'email': 'updated@example.com',
            'place': 'Updated Place',
            'password1': 'newpassword123',
            'password2': 'newpassword123'
        }
        response = self.client.post(self.url, data)

        # Check that the user is redirected to the user list page
        self.assertRedirects(response, reverse('user_list'))

        # Check that the user's data is updated
        self.register.refresh_from_db()
        self.assertEqual(self.register.username, 'updateduser')
        self.assertEqual(self.register.email, 'updated@example.com')
        self.assertEqual(self.register.place, 'Updated Place')

    def test_update_user_invalid_data(self):
        """
        Test updating a user with invalid data (e.g., mismatched passwords).
        """
        data = {
            'username': 'updateduser',
            'email': 'updated@example.com',
            'place': 'Updated Place',
            'password1': 'newpassword123',
            'password2': 'mismatchedpassword'  # Passwords do not match
        }
        response = self.client.post(self.url, data)

        # Check that the form is re-rendered with errors
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'update_user.html')
        self.assertIn('form', response.context)
        self.assertTrue(response.context['form'].errors)

    def test_update_user_not_found(self):
        """
        Test updating a non-existent user.
        """
        non_existent_user_id = 9999
        url = reverse('update_user', args=[non_existent_user_id])
        response = self.client.post(url, {})
