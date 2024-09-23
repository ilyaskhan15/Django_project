from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Member

def members(request):
    my_members =  Member.objects.all().values()
    template = loader.get_template('all_members.html')
    context = {
        'mymembers': my_members
    }
    return HttpResponse(template.render(context, request))

# Create your views here.
