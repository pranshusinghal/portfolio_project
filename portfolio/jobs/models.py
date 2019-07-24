from django.db import models

#Create your models here.
##	models are python classes that can 	
# 	be saved into the database
class Job(models.Model):
	#pip install pillow
	#above command allows django to work with images
	image = models.ImageField(upload_to='images/')
	summary = models.CharField(max_length=200)

	# returning summary for the jobs 
	def __str__(self):
		return self.summary


#	migrations are required to set up your database
#	we need to save models into the database
#	so we need to migrate

### commands
#	python3 manage.py makemigrations
#	python3 manage.py migrate