# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the poll index.")
    
# recall or note that %s means, "subsitute in a string"

def detail(request, poll_id):
    return HttpResponse("You're looking at poll <strong>%s</strong>." % (poll_id,))

def results(request, poll_id):
    return HttpResponse("You're looking at the results of poll %s." % (poll_id,))

def vote(request, poll_id):
    return HttpResponse("You're voting on poll %s." % (poll_id,))    
