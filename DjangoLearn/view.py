from django.http import HttpResponse,Http404
from django.shortcuts import  render
import  datetime

def hello(request):
    context = {}
    context['hello'] = 'hello world'
    return render(request,'hello.html',context)
    # return HttpResponse("hello world")



def currenttime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now

    return HttpResponse(html)

def hour_head(request,offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()

    now = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, now)
    return HttpResponse(html)