from django.shortcuts import render, get_object_or_404
## importing Jobs form database
from .models import Job

# Create your views here.
##	html files will be shown using views.py

def home(request):
	##	putting all Job objects in variable jobs
	jobs = Job.objects
	return render(request,'jobs/home.html',{'jobs':jobs})

def detail(request,job_id):
	#	get_object_or_404 
	# 	will return one object from database.
	job_detail = get_object_or_404(Job, pk = job_id)
	return render(request,'jobs/detail.html', {'job':job_detail})