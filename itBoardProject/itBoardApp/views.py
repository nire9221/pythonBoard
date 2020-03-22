from django.shortcuts import render
from django.shortcuts import render,get_object_or_404
from .models import Job
from .forms import JobForm
from django.contrib.auth.decorators import login_required

def index (request):
    return render(request, 'itBoardApp/index.html')

def getjobs(request):
    type_list=Job.objects.all()
    return render(request, 'itBoardApp/jobs.html' ,{'type_list' : type_list})

def getjobsdetails(request, id):
    job=get_object_or_404(Job, pk=id)
    return render(request, 'itBoardApp/jobsdetails.html',{'job' : job})

@login_required
def newJob(request):
     form=JobForm
     if request.method=='POST':
          form=JobForm(request.POST)
          if form.is_valid():
               post=form.save(commit=True)
               post.save()
               form=JobForm()
     else:
          form=JobForm()
     return render(request, 'itBoardApp/newjob.html', {'form': form})


def loginmessage(request):
    return render(request, 'itBoardApp/loginmessage.html')

def logoutmessage(request):
    return render(request, 'itBoardApp/logoutmessage.html')