from django.http import HttpResponse
from django.template import Context
from django.template.loader import get_template
from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect
from registration.models import *
from registration.forms import *
from datetime import datetime, date

def main_page(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            first_name     = form.cleaned_data['first_name']
            last_name      = form.cleaned_data['last_name']
            email          = form.cleaned_data['email']
            affiliation    = form.cleaned_data['affiliation']
            status         = form.cleaned_data['status']
            
            person, created = Person.objects.get_or_create(
                first_name=first_name,
                last_name=last_name,
                email=email,
                affiliation=affiliation,
                status=status
            )
            person.save()
            
            variables = RequestContext(request, {
                'person': person,
            })
            return render_to_response('registration_complete.html', variables)
    else:
        form = RegistrationForm()

    variables = RequestContext(request, {
        'form': form,
    })
    return render_to_response('registration.html', variables)

def add_session(request):
    if request.method == 'POST':
        form = SessionAdditionForm(request.POST)
        if form.is_valid():
            name        = form.cleaned_data['name']
            description = form.cleaned_data['description']
            leader      = form.cleaned_data['leader']
            place       = form.cleaned_data['place']
            time        = form.cleaned_data['time']
            size        = form.cleaned_data['size']
            
            session, created = Session.objects.get_or_create(
                name=name,
                description=description,
                leader=leader,
                place=place,
                time=time,
                size=size
            )
            session.save()
            
            variables = RequestContext(request, {
                'session': session
            })
            return render_to_response('session_added.html', variables)
    else :
        form = SessionAdditionForm()
    
    variables = RequestContext(request, {
        'form': form,
    })
    return render_to_response('add_session.html', variables)