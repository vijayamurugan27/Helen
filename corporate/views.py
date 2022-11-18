from django.shortcuts import render


from .models import Colleges
# Create your views here.
# def home1(request):
#     return render(request, 'corporate/home.html')

def colleges(request):
    colleges = Colleges.objects.all()
    context = {'colleges': colleges}
    return render(request, 'corporate/list.html', context)

# def home(request):
#     context = {}
#     return render(request, 'corporate/temp/index.html', context)

def about(request):
    context = {}
    return render(request, 'corporate/temp/about.html', context)

def blog(request):
    context = {}
    return render(request, 'corporate/temp/blog.html', context)

def portfolio(request):
    context = {}
    return render(request, 'corporate/temp/portfolio.html', context)

def contact(request):
    context = {}
    return render(request, 'corporate/temp/contact.html', context)



def base(request):
    context = {}
    return render(request, 'corporate/temp/base.html', context)

def index(request):
    context = {}
    return render(request, 'corporate/temp/index.html', context)

def index1(request):
    context = {}
    return render(request, 'corporate/temp/index1.html', context)