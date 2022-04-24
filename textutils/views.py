#This file created by Ankit Vaishnav
from django.http import HttpResponse
from django.shortcuts import render 

def index(request):
    return render(request,'index.html')

def analyze(request):
    text = request.POST.get('text','Default')
    punc = request.POST.get('removepunc','off')
    uppercase = request.POST.get('uppercase','off')
    newline = request.POST.get('newline','off')
    esremover = request.POST.get('esremover','off')
    title = ''
    
    if punc=='on':
        title += 'Remove Panctuations'
        analyzed_text = ''
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        for i in text:
            if i not in punctuations:
                analyzed_text += i
        text = analyzed_text
        
    if uppercase=='on':
        title += ' Change to Upper Case'
        analyzed_text1 = ''
        for i in text:
            analyzed_text1 += i.upper()
        text = analyzed_text1
        
    if newline =='on':
        title += ' Remove new Line'
        analyzed_text1 = ''
        for i in text:
            if i != '\n' and i!= '\r':
                analyzed_text1 += i.upper()
        text = analyzed_text1
        
    if esremover=='on':
        title += ' Exatra Spaces Remover'
        text = text.strip()
    
    params = {'porpose': title,'analyzed_Text': text}
    return render(request, 'analyze.html', params)
