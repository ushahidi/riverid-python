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
from face.forms import FaceForm
from mongoengine.django.auth import User
from face.models import Face
#m from pymongo.son import SON
import string

@login_required
def list_faces_admin(request, filter):
    """
    list users for administering
    currently filterable by active, inactive, admins, users
    #m to-do pagination
    """
    if not request.user.is_superuser:
        raise Http404
    
    filters = ['active', 'inactive', 'admins', 'users']

    if(filter == 'active'):
        entries = User.objects.filter(is_active=True).order_by('username')
    elif(filter == 'inactive'):
        entries = User.objects.filter(is_active=False).order_by('username')
    elif(filter == 'admins'):
        entries = User.objects.filter(is_superuser=True).order_by('username')
    elif(filter == 'users'):
        entries = User.objects.filter(is_superuser=False).order_by('username')
    else:
        entries = User.objects.filter().order_by('username')

    context = {
        'entries': entries,
        'title': 'Users',
        'filters': filters,
    }
    return render_to_response('face/list.html', context,
                              context_instance=RequestContext(request))
                              
@login_required
def edit(request, user=None):
    """
    User profile if upon POST save else render form
    """
    
    # define these values here for DRY copy&paste if,else logic
    form_class = FaceForm
    entry = Face.objects.get_or_create(user=request.user)
    
    if request.method == 'POST':
        form = form_class(request.POST)
        if form.is_valid():
            # Get necessary post data from the form
            for field, value in form.cleaned_data.items():
                if field in entry._fields.keys():
                    entry[field] = value
            entry.save()
            return HttpResponseRedirect(entry.get_absolute_url())
    else:
        fields = entry._fields.keys()
        field_dict = dict([(name, entry[name]) for name in fields])
        
        form = form_class(field_dict)

    context = {
        'title': 'Edit your profile',
        'form': form,
    }
    return render_to_response('face/edit.html', context,
                              context_instance=RequestContext(request))
                              
def detail(request, username):
    """
    Render User profile page, this is going to be big later, listing user activities
    across various Swift sites and user reputation
    """
    user = User.objects(username=username).first()
    if not user:
        raise Http404
    
    face = Face.objects(user=user).first()

    context = {
        'title': 'User\'s Profile',
        'face': face,
    }
    return render_to_response('face/detail.html', context,
                              context_instance=RequestContext(request))

@login_required
def delete_face(request):
    """
    Delete user as well as profile
    do not allow deletion of own account by admin though
    admin can delete one another as of now
    """
    if not request.user.is_superuser:
        raise Http404

    entry_id = request.POST.get('entry_id', None)
    if request.method == 'POST' and entry_id:
        u = User.objects.with_id(entry_id)
        
        #m to-do better find a replacement for Http404
        if u.id == request.user.id:
            raise Http404
            
        f = Face.objects.get(user=u)
        
        u.delete()
        f.delete()
               
    return HttpResponseRedirect(reverse('face_list_admin', args=['all']))

@login_required
def active_face(request):
    """
    Make user active, wrapping around mongoengine.django.auth
    """
    if not request.user.is_superuser:
        raise Http404

    entry_id = request.POST.get('entry_id', False)
    entry_status = request.POST.get('entry_status', False)
    if request.method == 'POST' and entry_id:
        entry = User.objects.with_id(entry_id)
        entry.is_active = bool(entry_status)
        entry.save()

    return HttpResponseRedirect(reverse('face_list_admin', args=['all']))

@login_required
def admin_face(request):
    """
    Make user admin, wrapping around mongoengine.django.auth
    do not allow making oneself a user
    """
    if not request.user.is_superuser:
        raise Http404

    entry_id = request.POST.get('entry_id', None)
    entry_status = request.POST.get('entry_status', False)
    if request.method == 'POST' and entry_id:
        entry = User.objects.with_id(entry_id)
        
        #m to-do better find a replacement for Http404
        if entry.id == request.user.id and bool(entry_status):
            raise Http404
            
        entry.is_superuser = bool(entry_status)
        entry.save()

    return HttpResponseRedirect(reverse('face_list_admin', args=['all']))