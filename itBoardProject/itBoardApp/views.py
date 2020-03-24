from django.shortcuts import render, get_object_or_404
from .models import Event
from .forms import EventForm


def index(request):
    return render(request, 'itBoardApp/index.html')


def getEvent(request):
    event_list = Event.objects.all()
    return render(request, 'itBoardApp/event.html', {'event_list': event_list})


def eventDetail(request, id):
    detail = get_object_or_404(Event, pk=id)

    return render(request, 'itBoardApp/eventDetail.html', {'detail': detail})


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
