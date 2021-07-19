"""Register Topic with the admin site.

This code imports the model we want to register, Topic, and then uses
admin.site.reigster() to tell Django to manage our model through the admin site
"""

from django.contrib import admin

# Register your models here.
from learning_logs.models import Topic, Entry

admin.site.register(Topic)
admin.site.register(Entry)
