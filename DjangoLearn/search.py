# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.shortcuts import  render_to_response

from django.shortcuts import render
from books.models import  Book



def search_form(request):

    print "path:" + request.path


    if request.POST:
        print 'search_form post method'
    else:
        print 'search_form get method'

    return render_to_response("search_form.html")



def search(request):

    request.encoding="UTF-8"

    print "path:" + request.path



    if 'q' in request.GET:
        message='你搜索的内容为：' + request.GET['q'].encode('UTF-8')

        q = request.GET['q']
        books = Book.objects.filter(title__icontains=q)
        return render_to_response('search_result.html',
                              {'books': books, 'query': q})
    else:
        message = '你搜索的内容为空'

    return HttpResponse(message)



def search_post(request):
    ctx = {}
    # ctx.update(csrf(request))


    print "path:" + request.path

    if request.POST:
        print 'search_post post method'
    else:
        print 'search_post get method'


    if request.POST:
        ctx['rlt'] = request.POST['q']
    return render(request, "search_post.html", ctx)

