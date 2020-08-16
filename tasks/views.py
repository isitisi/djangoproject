from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib.auth import logout

from tasks.models import daily_Tasks
# Create your views here.
def index(request):
	return render(request, 'index.html', {
		'todays_task': daily_Tasks.objects.all()
		})
