from django.shortcuts import render

# Create your views here.


def index(request):
    mydict = {'text': 'hello world', 'number': 100}
    return render(request, 'urlapp/index.html', context=mydict)


def other(request):
    return render(request, 'urlapp/other.html')


def relative(request):
    return render(request, 'urlapp/relative_url_template.html')
