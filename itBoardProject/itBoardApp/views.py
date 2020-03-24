from django.shortcuts import  *
from .models import Genre, Article
from .forms import ArticleForm
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

def loginmessage(request):
    return render(request, 'itBoardApp/loginmessage.html')

def logoutmessage(request):
    return render(request, 'itBoardApp/logoutmessage.html')