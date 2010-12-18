from django.http import HttpResponse, Http404, HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
#m from django.contrib.auth.forms import AuthenticationForm
#m from django.core.paginator import Paginator, InvalidPage, EmptyPage
#m from django.conf import settings
#m from django.contrib.syndication.feeds import Feed
#m from django.utils.feedgenerator import Atom1Feed
from django.template import defaultfilters


from mongoengine.django.auth import User
from face.models import Face
from piston.models import Consumer, Token, Nonce

def feedfish(request):
    
    # don't let add anymore if there is a user
    if User.objects.count():
        raise Http404
        
    # create an admin user
    admin = User.objects.create_user('admin', 'admin@admin.com', 'admin')
    admin.is_active = True
    admin.is_superuser = True
    admin.save()

    face = Face.objects.get_or_create(user=admin)
    face.first_name = 'Admin'
    face.last_name = 'Admin'
    face.about = 'I am site admin! I am super!'
    face.save()
        
    # create a test user
    user = User.objects.create_user('user', 'user@user.com', 'user')
    user.is_active = True
    user.save()
    
    face = Face.objects.get_or_create(user=user)
    face.first_name = 'User'
    face.last_name = 'User'
    face.about = 'I am just a user. This is my profile'
    face.save()
    
    # create a dev user
    dev = User.objects.create_user('dev', 'dev@dev.com', 'dev')
    dev.is_active = True
    dev.save()
    
    face = Face.objects.get_or_create(user=dev)
    face.first_name = 'Admin'
    face.last_name = 'Admin'
    face.about = 'I am a developer! I have a API key! I could get more if I am greedy! \
                    I like fishing in river. Huh!'
    face.save()
    
    # create a Consumer / API Key for dev (it is all preset in oauth_client.py)
    key = Consumer.objects.get_or_create(user=dev)
    key.name = 'First RiverID App'
    key.url = 'http://app-amazon.com'
    key.description = 'Crowdsourcing for wildlife in Amazon basin'
    
    key.status = 'accepted'
    key.key =   'pwnDkTNskHsWdnBrAc'
    key.secret = 'PMXV6LAJYgw2MAbGY9s39um6m9Jvjxgn'
    key.save()
    
    context = {
        'base_title': 'Feeding fishes',
        'base_content': 'It was easy. 3 users are created: \n admin, user, dev ...\n \
                        passwords are same as usernames. To test for OAuth, run oauth_client.py, \
                        it has the API Conumser key/secret set already.',
    }
    return render_to_response('base.html', context,
                              context_instance=RequestContext(request))    

@login_required
def killoil(request):

    if not request.user.is_superuser:
        raise Http404

    for f in Face.objects:
        f.delete()
        
    for u in User.objects:
        u.delete()
        
    for c in Consumer.objects:
        c.delete()
        
    for t in Token.objects:
        t.delete()
        
    for n in Nonce.objects:
        n.delete()

    context = {
        'base_title': 'Killing oil',
        'base_content': 'Wouldn\'t world be a better place without oil? Just cleared the database. \
        Feed fish again to make the river lively...',
    }
    return render_to_response('base.html', context,
                            context_instance=RequestContext(request))    
    
    
        
    
    
