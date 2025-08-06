from django import forms
from .models import Report
from django import forms
from .models import Report

from django import forms
from .models import Report

from django import forms
from .models import Report

class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ['name', 'email', 'phone_number', 'description', 'photo', 'status']

    location = forms.CharField(widget=forms.HiddenInput())  # For storing the location data
from django import forms
from django.core.exceptions import ValidationError
from accounts.models import Register ,Register2,Register3 # Adjust based on your structure
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate


class RegisterForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Register  # Your Register model
        fields = ['username', 'birthday', 'place','email', 'password1', 'password2']

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            self.add_error('password2', "Passwords do not match.")  # Attach the error to the second password field

        return cleaned_data


from django import forms
from .models import Register2

# In your forms.py

class RegisterForm2(forms.ModelForm):
    class Meta:
        model = Register2
        fields = ['username', 'specialization', 'work', 'email', 'password1', 'password2']

    def save(self, commit=True):
        instance = super().save(commit=False)

        # Create or associate a user object
        if commit:
            # You can create the user in the same view as shown above
            user = User.objects.create_user(
                username=self.cleaned_data['username'],
                password=self.cleaned_data['password1'],
                email=self.cleaned_data['email']
            )
            instance.user = user  # Set the user

            instance.save()
        return instance

from django import forms

class RegisterForm3(forms.ModelForm):
    class Meta:
        model = Register3
        fields = ['username', 'work', 'email', 'department', 'phone', 'password1', 'password2']
        widgets = {
            'password1': forms.PasswordInput(),
            'password2': forms.PasswordInput(),
        }

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            self.add_error('password2', "Passwords do not match.")

from django import forms
from .models import Login_3

class Login3Form(forms.ModelForm):
    class Meta:
        model = Login_3
        fields = ['username', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }
# forms.py
from django import forms

from django import forms

from django import forms
from .models import Rating

class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ['rating', 'comment']
