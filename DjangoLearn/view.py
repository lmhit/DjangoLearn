from django.http import HttpResponse,Http404
from django.shortcuts import  render
import  datetime

def hello(request):



    context = {}
    context['hello'] = 'hello world'
    return render(request,'hello.html',context)
    # return HttpResponse("hello world")



def currenttime(request):

    try:
        ua = request.META['HTTP_USER_AGENT']

    except KeyError:
        ua = 'unknow'

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



def display_meta(request):
    values = request.META.items()
    values.sort()
    html = []
    for k, v in values:
        html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, v))
    return HttpResponse('<table>%s</table>' % '\n'.join(html))




def testConfig(request,GET=None,POST=None):
    if request.method == 'GET'  and GET is not None:
        return GET(request)
    elif request.method == 'POST' and POST is not  None:
        return POST(request)
    else:
        return Http404()



def testGet(request):
    # if(request.method == 'GET'):
    assert  request.method == 'GET'

    return HttpResponse("test GET")


def testPost(request):
    # if(request.method == 'POST'):
    assert request.method == 'POST'

    return HttpResponse("test POST")


