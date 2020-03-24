from django.shortcuts import  *
from django.shortcuts import render,get_object_or_404
from .models import Genre, Article, Job, Event
from .forms import ArticleForm, JobForm, EventForm
from django.contrib.auth.decorators import login_required

@login_required
def index (request):
    return render(request, 'itBoardApp/index.html')

@login_required
def getarticle (request):
    article_list=Article.objects.all()
    return render(request, 'itBoardApp/article.html', {'article_list' : article_list})

@login_required
def getarticledetail (request, id):
    article_detail=get_object_or_404(Article, pk=id)
    return render(request, 'itBoardApp/articledetail.html', {'article_detail' : article_detail})

@login_required
def newArticle(request):
     form=ArticleForm
     if request.method=='POST':
          form=ArticleForm(request.POST)
          if form.is_valid():
               post=form.save(commit=True)
               post.save()
               form=ArticleForm()
     else:
          form=ArticleForm()
     return render(request, 'itBoardApp/newArticle.html', {'form': form})

@login_required
def getjobs(request):
    type_list=Job.objects.all()
    return render(request, 'itBoardApp/jobs.html' ,{'type_list' : type_list})

@login_required
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
@login_required
def getEvent(request):
    event_list = Event.objects.all()
    return render(request, 'itBoardApp/event.html', {'event_list': event_list})

@login_required
def eventDetail(request, id):
    detail = get_object_or_404(Event, pk=id)

    return render(request, 'itBoardApp/eventDetail.html', {'detail': detail})

@login_required
def newEvent(request):
    form = EventForm
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            post = form.save(commit=True)
            post.save()
            form = EventForm()
    else:
        form = EventForm()
    return render(request, 'itBoardApp/newevent.html', {'form': form})


def loginmessage(request):
    return render(request, 'itBoardApp/loginmessage.html')

def logoutmessage(request):
    return render(request, 'itBoardApp/logoutmessage.html')