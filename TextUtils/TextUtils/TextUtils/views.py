from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    #return HttpResponse("this is home page")
    return render(request,'index2.html')

def removepunc(request):
    dtext= request.POST.get('text', 'default')
    chbox = request.POST.get('removepunc', 'off')
    charcount = request.POST.get('charcount', 'off')
    extraspace = request.POST.get('extraspace', 'off')
    capetalize = request.POST.get('capetalize', 'off')


    if chbox == 'on':
        punctuations = '''!"#$%&'()*+, -./:;<=>?@[\]^_`{|}~'''
        analyze = ""
        for char in dtext:
            if char not in punctuations:
                analyze=analyze+char
        dict = {'original': dtext, 'rt': analyze}
        dtext = analyze
        #return render(request, 'next.html', dict)
    if (capetalize == 'on'):
        analyze = ""
        for char in dtext:
            analyze = analyze + char.upper()
        dict = {'original': dtext, 'rt': analyze}
        dtext = analyze

    if(extraspace == 'on'):
        analyze = ""
        for index, char in enumerate(dtext):
            if(dtext1[index] == " " and dtext1[index+1]==" "):
                pass
            else:
                analyze = analyze + char

        dict = {'original': dtext, 'rt': analyze}
        dtext = analyze
        #return render(request, 'next.html', dict)

    if(chbox != 'on' and capetalize != 'on'):
        return HttpResponse("error")
    return render(request, 'next.html', dict)

    # if (charcount == 'on'):
    #     count = 0
    #     for char in dtext:
    #         count = count + 1
    #     dict = {'original': dtext, 'nochr': count}
    #     dtext = analyze
    #     # return render(request, 'next.html',dict)

