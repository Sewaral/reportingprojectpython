from django.contrib import admin
from django.utils.html import format_html
from .models import Report

from django.contrib import admin
from .models import Report


from django.contrib import admin
from .models import Report

class ReportAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'status', 'created_at', 'updated_at')
    readonly_fields = ('created_at', 'updated_at')
    list_filter = ('status', 'created_at')
    exclude = ('status',)  # Hide the 'status' field from the admin form

admin.site.register(Report, ReportAdmin)



# Register your models here.
from django.contrib import admin
from .models import *

from accounts.models import Login_1,Login_2,Register,Register2
from accounts.models import Login_3,Register,Register3

class RegisterAdmin(admin.ModelAdmin):
    list_display = ('username', 'email')
    search_fields = ('username', 'email')
    ordering = ('username',)

from django.contrib import admin
from .models import Register2, Login_2

class RegisterAdmin2(admin.ModelAdmin):
    list_display = ('username', 'email')
    search_fields = ('username', 'email')
    ordering = ('username',)

admin.site.register(Register2, RegisterAdmin2)
admin.site.register(Login_2)

admin.site.register(Register, RegisterAdmin)

admin.site.register(Register3, RegisterAdmin)
admin.site.register(Login_3)

admin.site.register(Login_1)
from django.contrib import admin

from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Message

class MessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'content', 'timestamp')  # הצגת שם המשתמש, תוכן ההודעה וזמן ההודעה
    search_fields = ('name', 'content')  # חיפוש לפי שם המשתמש ותוכן ההודעה
    list_filter = ('timestamp',)  # סינון לפי תאריך
    ordering = ('-timestamp',)  # מיון לפי זמן ההודעה (מהחדש לישן)

admin.site.register(Message, MessageAdmin)
from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Rating

class RatingAdmin(admin.ModelAdmin):
    list_display = ('rating', 'comment', 'created_at')  # Columns displayed in the list view
    list_filter = ('rating',)  # Add filtering by rating
    search_fields = ('comment',)  # Add search functionality for comments
    ordering = ('-created_at',)  # Order by creation date (newest first)

admin.site.register(Rating, RatingAdmin)