##   admin allows us to work with database

from django.contrib import admin
#import your models here
from .models import Job


# Register your models here.
admin.site.register(Job)

##  we need to create a superuser to login to admin
#   python manage.py createsuperuser


## add jobs(image and summary) in admin page
##  Job.object will be created