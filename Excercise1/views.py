#I have created this file -Akshay

from django.http import HttpResponse
from django.shortcuts import render


#code for video-7
def index(request):

    return render(request, 'index.html')
    #return HttpResponse('''<h1>Home</h1>''')

def analyze(request):
    #Get the text
    djtext = request.POST.get('text', 'default')

    # check checkbox values
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps  = request.POST.get('fullcaps', 'off')
    newlineremover  = request.POST.get('newlineremover', 'off')
    extraspaceremover  = request.POST.get('extraspaceremover', 'off')
    # charcount  = request.POST.get('charcount', 'off')

    #check which checkbox is on
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = " "
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char


        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        djtext = analyzed
        #return render(request, 'analyze.html', params)

    if (fullcaps == "on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()

        params = {'purpose': 'changed to Uppercase', 'analyzed_text': analyzed}
        djtext = analyzed
        # Analyze the text
        #return render(request, 'analyze.html', params)

    if(newlineremover=="on"):
        analyzed = ""
        for char in djtext:
            if char !="\n" and char !="\r":
                analyzed = analyzed + char

        params = {'purpose': 'Removed new lines', 'analyzed_text': analyzed}
        djtext = analyzed
        # Analyze the text
        #return render(request, 'analyze.html', params)

    if(extraspaceremover=="on"):
        analyzed = ""
        for index, char in enumerate (djtext):
            if not (djtext[index] == " " and djtext[index+1] ==" "):

                analyzed = analyzed + char

        params = {'purpose': 'Removed new lines', 'analyzed_text': analyzed}
        djtext = analyzed
        # Analyze the text
        #return render(request, 'analyze.html', params)

    # if (charcount == 'on'):
    #     analyzed = djtext
    #
    #
    #     params = {'purpose': 'Counting Characters', 'analyzed_text': len(analyzed)}
    #     djtext = analyzed
    #     #return render(request, 'analyze.html', params)

    return render(request, 'analyze.html', params)










































    # code for video-6
    # def index(request):
    #     return HttpResponse(''' <h1> Hello, This is Akshay </h1> <a href="https://www.facebook.com/"> Facebook.com</a>>''')
    #
    # def codewithharry(request):
    #     return HttpResponse(''' <h1> Hello, This is code with harry website </h1> <a href="https://www.codewithharry.com/"> code with harry</a>>''')
    #
    # def about(request):
    #     return HttpResponse("this is about page")

# def capfirst(request):
#     return HttpResponse('''<h1>capitalize first</h1> <a href="http://127.0.0.1:8000/"><button>Back</button></a>''')
#
# def newlineremove(request):
#     return HttpResponse('''<h1>new line remove</h1> <a href="http://127.0.0.1:8000/"><button>Back</button></a>''')
#
# def spaceremove(request):
#     return HttpResponse('''<h1>space remove</h1> <a href="http://127.0.0.1:8000/"><button>Back</button></a>''')
#
# def charcount(request):
#     return HttpResponse('''<h1>charcount</h1> <a href="http://127.0.0.1:8000/"><button>Back</button></a>''')