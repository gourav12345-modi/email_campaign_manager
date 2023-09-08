from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse

from .models import Subscribers

def unsubscribe_user(request, email):
    subscriber = get_object_or_404(Subscribers, email=email)
    
    if request.method == 'GET':
        subscriber.is_active = False
        subscriber.save()
        return HttpResponse('You have been unsubscribed successfully.')
