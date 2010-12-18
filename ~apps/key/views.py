from django.http import HttpResponse, Http404, HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
#m from django.contrib.auth.forms import AuthenticationForm
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.conf import settings
#m from django.contrib.syndication.feeds import Feed
#m from django.utils.feedgenerator import Atom1Feed
from django.template import defaultfilters

from datetime import datetime, time
from mongoengine.django.auth import REDIRECT_FIELD_NAME
from mongoengine.django.auth import User
from piston.models import Consumer, Token
from forms import ConsumerForm
#m from pymongo.son import SON
import string

@login_required
def list_consumers(request):
    """
    list oauth consumers 
    i.e: external sites and apps that has key to access Swift APIs
    """
    entries = Consumer.objects.filter(user=request.user).order_by('name')

    context = {
        'entries': entries,
        'title': 'Your API Keys',
    }
    return render_to_response('key/list.html', context,
                              context_instance=RequestContext(request))

@login_required
def list_consumers_admin(request, status):
    """
    list oauth consumers for administering
    i.e: external sites and apps that has key to access Swift APIs
    #m to-do pagination
    """
    if not request.user.is_superuser:
        raise Http404
    
    statuses = ['pending', 'accepted', 'canceled', 'rejected']
    
    if status == 'all':
        entries = Consumer.objects.filter().order_by('name')
    elif status in statuses:
        entries = Consumer.objects.filter(status=status).order_by('name')
    else:
        raise Http404
    
    context = {
        'entries': entries,
        'title': 'Manage API Keys',
        'admin': True,
        'statuses': statuses,
    }
    return render_to_response('key/list.html', context,
                                context_instance=RequestContext(request)) 
                                                             
@login_required
def edit_consumer(request, consumer_id):
    """
    Piston Consumer form if upon POST save else render form
    Editing existing API key
    """
    
    # define these values here for DRY copy&paste if,else logic
    form_class = ConsumerForm
    entry = Consumer.objects.with_id(consumer_id)
    if not entry:
        raise Http404
    
    if entry.user.id != request.user.id:
        raise Http404
    
    if request.method == 'POST':
        form = form_class(request.POST)
        if form.is_valid():
            # Get necessary post data from the form
            for field, value in form.cleaned_data.items():
                if field in entry._fields.keys():
                    entry[field] = value
            entry.save()
            return HttpResponseRedirect(reverse('key_list'))
    else:
        fields = entry._fields.keys()
        field_dict = dict([(name, entry[name]) for name in fields])
        
        form = form_class(field_dict)

    context = {
        'title': 'Edit your API key',
        'form_button': 'Save your API info',
        'form': form,
        'entry': entry,
    }
    
    return render_to_response('key/edit.html', context,
                              context_instance=RequestContext(request))

@login_required
def add_consumer(request):
    """
    Piston Consumer form if upon POST save else render form
    New API key request
    """

    form_class = ConsumerForm
    entry_class = Consumer

    if request.method == 'POST':
      form = form_class(request.POST)
      if form.is_valid():
          
          entry = Consumer(**form.cleaned_data)
          entry.user = request.user
          entry.key, entry.secret = Consumer.objects.generate_random_codes()
          entry.status = 'pending'

          # Save the entry to the DB
          entry.save()
          return HttpResponseRedirect(reverse('key_list'))
    else:
      initial = {
      }

      form = form_class(initial=initial)

    context = {
        'title': 'Get an API key',
        'form_button': 'Get the key NOW!',
        'form': form,
    }
      
    return render_to_response('key/edit.html', context,
                            context_instance=RequestContext(request))
                            
@login_required
def delete_consumer(request):
    """
    Delete API key
    """
    entry_id = request.POST.get('entry_id', None)
    if request.method == 'POST' and entry_id:
        entry = Consumer.objects.with_id(entry_id)
        if entry.user.id == request.user.id:
            entry.delete()
            
    return HttpResponseRedirect(reverse('key_list'))

@login_required
def delete_consumer_admin(request):
    """
    Delete API key by admin
    """
    if not request.user.is_superuser:
        raise Http404
        
    entry_id = request.POST.get('entry_id', None)
    if request.method == 'POST' and entry_id:
        entry = Consumer.objects.with_id(entry_id)
        if request.user.is_superuser:
            entry.delete()

    return HttpResponseRedirect(reverse('key_list_admin', args=['all']))
        
@login_required
def status_consumer(request):
    """
    Change API key status by admin
    """
    if not request.user.is_superuser:
        raise Http404
        
    entry_id = request.POST.get('entry_id', None)
    entry_status = request.POST.get('entry_status', None)
    if request.method == 'POST' and entry_id and entry_status:
        entry = Consumer.objects.with_id(entry_id)
        entry.status = entry_status
        entry.save()

    return HttpResponseRedirect(reverse('key_list_admin', args=['all']))

@login_required
def list_tokens(request):
    """
    list authorizations by a particular user
    """
    entries = Token.objects.filter(user=request.user).order_by('name')

    context = {
        'entries': entries,
        'title': 'Your authorized sites/apps',
    }
    return render_to_response('key/tokens.html', context,
                              context_instance=RequestContext(request))
                              
@login_required
def oauth_callback(request, token):
    return HttpResponse('This is the verifier PIN: '+ str(token.verifier), mimetype="text/plain")