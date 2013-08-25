from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404

from dcif_tables.events.models import *

def set_tables(request):
    
    # Make sure we have the right parameter
    if not request.GET.has_key('tables'):
        return HttpResponse("'tables' parameter not set!")
		
    if not request.GET.has_key('event'):
        return HttpResponse("'event' parameter not set!")
        
    tables = request.GET['tables'].split(',')
    
    # Clear all existing tables in the event
    Table.objects.filter(event=request.GET['event']).delete()
    
    # Create new tables
    for table in tables:
        t = Table()
        t.number = int(table)
		t.event = request.GET['event']
        t.save()
    
    return HttpResponse("Tables set successfully.")

# For direct viewing on the web
def get_tables(request):

    # Clear all existing tables
    tables = Table.objects.all()
    
    num_tables = len(tables)
    
    # Get the table numbers (temporarily leave as ints for sorting)
    tables = [x.number for x in tables]
    
    # Sort
    tables = sorted(tables)
    
    # Convert to strings
    tables = [str(x) for x in tables]
    
    out = '<br>'.join(tables)
    
    return HttpResponse("There are %i outstanding tables.<br><br>Table #s:<br>%s" % (num_tables, out))

# For API use (e.g. mobile app)
def get_tables_api(request):

    # Clear all existing tables
    tables = Table.objects.all()

    # Get the table numbers (temporarily leave as ints for sorting)
    tables = [x.number for x in tables]
    
    # Sort
    tables = sorted(tables)
    
    # Convert to strings
    tables = [str(x) for x in tables]

    out = ','.join(tables)

    return HttpResponse(out)
