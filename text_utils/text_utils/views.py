#created by rahul.

#utilites/packages:
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    '''
    a = 'Home'
    return HttpResponse(a)
    '''
    #u can pass variables to render as arguements and access in html file
    params = {'creator':'Rahul','location':'Bengaluru','email':'rahuljoshey187@gmail.com'}

    #to obtain input given/text given to html code
    return render(request,'index 2.html')

def about(request):
    b = '''
    about Text Utils
    <br>
    <button> <a href= / > Back! </a> </button>
    '''
    return HttpResponse(b)

def analyze(request):
   #getting text
    djtext = request.POST.get('text','Default')
    #print(djtext)
    
    #getting method
    removepunc = request.POST.get('removepunc','off')
    capitalize = request.POST.get('capitalize','off')
    newlineremove = request.POST.get('newlineremove','off')
    extraspaceremove = request.POST.get('extraspaceremove','off')
    charcount = request.POST.get('charcount','off')
    #print(removepunc)

    #defaults
    purp = 'select an option'
    analyzed_txt = ''


    #analyzing text
    if removepunc == 'on':
        purp = 'Remove Punctuations'
        puncs = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed_txt = ''
        for char in djtext:
            if char not in puncs:
                analyzed_txt += char
        
        #to give result when multiple buttons are pressed
        djtext = analyzed_txt
        
    if capitalize == 'on':
        purp = 'Capitalize'
        analyzed_txt = ""
        for char in djtext:
            analyzed_txt += char.upper()
        djtext = analyzed_txt
    if newlineremove == 'on':
        purp = 'Remove New Line'
        analyzed_txt = ''
        for char in djtext:
            if char != '\n'and char!='\r':
                analyzed_txt += char
        djtext = analyzed_txt
    if extraspaceremove == 'on':
        purp = 'Remove Extra Space'
        analyzed_txt = ''
        for index,char in enumerate(djtext):
            if not(djtext[index] == ' ' and djtext[index + 1] == ' '):
                analyzed_txt += char
        djtext = analyzed_txt
    if charcount == 'on':
        purp = 'Count the Characters'
        cnt = 0
        analyzed_txt = ''
        for char in djtext:
            if (char != ' '):
                cnt += 1
        analyzed_txt = "No, of characters in text are: " + str(cnt)
        djtext = analyzed_txt
    #returning solution
    params = {'purpose': purp, 'result':analyzed_txt}
    return render(request,'analyze 2.html',params)

