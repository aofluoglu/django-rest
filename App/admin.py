from django.contrib import admin

# Register your models here.
from App.models import UserProfile, UserSkills

admin.site.register(UserProfile)
admin.site.register(UserSkills)
