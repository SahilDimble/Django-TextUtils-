#I have created this file - Sahil
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    #return HttpResponse("hello")
    return render(request, 'index.html')

def analyze(request):
    djtext=request.POST.get('text','default')
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    spaceremover = request.POST.get('spaceremover', 'off')
    charcount = request.POST.get('charcount', 'off')

    if removepunc== "on":
        punctuations='''!()-[]{};:'",<>?./~@#$%^&*'''
        analyzed=""
        for char in djtext:
            if char not in punctuations:
                analyzed=analyzed+char
        params={'purpose':'Removed Punctuations','analyzed_text':analyzed}
        djtext=analyzed
        #return render(request,'analyze.html',params)

    if(fullcaps=="on"):
        analyzed=""
        for char in djtext:
            analyzed=analyzed+char.upper()
        params={'purpose':'Changed to Uppercase','analyzed_text':analyzed}
        djtext = analyzed
        #return render(request,'analyze.html',params)

    if(newlineremover=="on"):
        analyzed = ""
        for char in djtext:
            if char!="\n" and char!='\r':
                analyzed = analyzed + char
        params = {'purpose': 'Removed New Lines', 'analyzed_text': analyzed}
        djtext = analyzed
        #return render(request, 'analyze.html', params)

    if(spaceremover == "on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index+1]==" "):
                analyzed = analyzed + char
        params = {'purpose': 'Removed Spaces', 'analyzed_text': analyzed}
        djtext = analyzed
        #return render(request, 'analyze.html', params)

    if(charcount == "on"):
        count=0
        for i in djtext:
            count +=1
        params = {'purpose': 'Char count', 'analyzed_text': count}

    if(removepunc!="on" and newlineremover!="on" and spaceremover!="on" and charcount!="on" and fullcaps!="on"):
        return HttpResponse("You haven't select any options, that's why you are seeing this message...!")


    return render(request, 'analyze.html', params)
