from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Job
# Register your models here.

@admin.register(Job)
class Job_admin(admin.ModelAdmin):
    list_display = ("Company", "Location", "JD", "posted", "job_role")