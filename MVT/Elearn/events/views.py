from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .models import Event

# Create your views here.
def event_list_view(request):
    object_list = Event.objects.filter(active=True)
    paginator = Paginator(object_list, 6)
    page = request.GET.get('page')
    
    try:
        events = paginator.page(page)
    except PageNotAnInteger:
        events = paginator.page(1)
    except EmptyPage:
        events = paginator.page(paginator.num_pages)
    
    context = {
        'events': events,
    }
    
    return render(request, 'events/event_list.html', context=context)

def event_detail_view(request, date, slug):
    event =get_object_or_404(Event, event_day=date, slug=slug)
    
    context = {
        'event': event,
    }
    
    return render(request, 'events/event_detail.html', context=context)
