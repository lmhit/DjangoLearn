from django.http import  HttpResponse

from django.shortcuts import  render

from DjangoModel.models import  Test
def adddb(request):

    test1 = Test(name ="lmhit test1")
    test1.save()
    return HttpResponse("<p> save data  success! <p>")


def getItem(request):

    response =""
    response1 = ""

    list = Test.objects.all()

    result = list.count()


    for var in list:
        response1 += var.name + "  "

    response = response1

    return HttpResponse("<p>" + response + "<p>")