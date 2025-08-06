from django.db import models

# Create your models here.
from django.core.validators import MinLengthValidator
from django.db import models

class Engineer(models.Model):
    name = models.CharField(max_length=100)
    # other fields related to the engineer

    def __str__(self):
        return self.name

from django.db import models

from django.db import models

from django.db import models

class Report(models.Model):
    STATUS_CHOICES = [
        ('open', 'Open'),
        ('in_progress', 'In Progress'),
        ('done', 'Done'),
    ]

    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    description = models.TextField()
    photo = models.ImageField(upload_to='reports/photos/', blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default='open'
    )
    created_at = models.DateTimeField(auto_now_add=True)  # Automatically set when the record is created
    updated_at = models.DateTimeField(auto_now=True)  # Automatically set whenever the record is updated

    def __str__(self):
        return f"Report by {self.name}"





from django.db import models
# adding changes :)
# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.models import User

# Create your models here.
class Register(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # ForeignKey to User
    username = models.CharField(max_length=50)
    birthday = models.DateField(null=True, blank=True)  # Allow null values
    email = models.EmailField()
    place=models.CharField(max_length=50)
    password1 = models.CharField(max_length=20)
    password2 = models.CharField(max_length=20)

    def __str__(self):
        return self.username

class Login_1(models.Model):#citezen
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # ForeignKey to the User model
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=128)

from django.db import models
from django.contrib.auth.models import User

class Register2(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # ForeignKey to User
    username = models.CharField(max_length=50)
    specialization  = models.CharField(max_length=15)
    work = models.CharField(max_length=15)
    email = models.EmailField()
    password1 = models.CharField(validators=[MinLengthValidator(8)], max_length=20)
    password2 = models.CharField(max_length=20)

    def __str__(self):
        return self.username

class Login_2(models.Model):#engenner
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # ForeignKey to the User model
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=128)

from django.db import models

class Login_3(models.Model):#engenner
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # ForeignKey to the User model
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=128)
from django.db import models
from django.contrib.auth.models import User

class Register3(models.Model): #worker
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # ForeignKey to User
    username = models.CharField(max_length=50)
    work = models.CharField(max_length=15)
    email = models.EmailField()
    department=models.CharField(max_length=15)
    phone=models.CharField(max_length=15)
    password1 = models.CharField(validators=[MinLengthValidator(8)], max_length=20)
    password2 = models.CharField(max_length=20)

    def __str__(self):
        return self.username
from django.db import models

class Message(models.Model):
    name = models.CharField(max_length=100, default="Anonymous")  # שם משתמש
    content = models.TextField()  # תוכן ההודעה
    timestamp = models.DateTimeField(auto_now_add=True)  # זמן יצירת ההודעה

    def __str__(self):
        return f"{self.name}: {self.content[:20]}"  # הצגה קצרה של ההודעה
from django.db import models


class Rating(models.Model):
    RATING_CHOICES = [
        (1, '1 Star'),
        (2, '2 Stars'),
        (3, '3 Stars'),
        (4, '4 Stars'),
        (5, '5 Stars'),
    ]

    rating = models.IntegerField(choices=RATING_CHOICES, verbose_name="Rating")
    comment = models.TextField(blank=True, null=True, verbose_name="Comment")  # Optional comment
    created_at = models.DateTimeField(auto_now_add=True,
                                      verbose_name="Created At")  # Timestamp when the rating was created

    def __str__(self):
        return f"Rating: {self.rating} - {self.comment[:50]}"  # Display the first 50 characters of the comment

    class Meta:
        verbose_name = 'Rating'
        verbose_name_plural = 'Ratings'
        ordering = ['-created_at']  # Order ratings by creation date (newest first)