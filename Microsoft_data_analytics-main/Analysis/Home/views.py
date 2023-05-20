from django.http import HttpResponseRedirect
from django.shortcuts import render, HttpResponse,HttpResponseRedirect
# from matplotlib.style import context
from . import data_info, data_info_cylinder
from .forms import UserDataFrom,InputForm
# Create your views here.
from . import query


def fun(a,b):
    print(a,b)

def index(request):
    return render(request, 'home.html')
    # return HttpResponse("Hello")

#def home_view(request):
    

def analysis(request):
    # context['graph'] = data_info.get_graph_cylinder()
    # graph = data_info_cylinder.get_graph_cylinder()
    # graph2 = data_info.get_graph_fuel_type()
    return render(request, 'DataAnalysis.html' )


def customer(request):
    if request.method == "POST":
        print("Hello")
        data = InputForm(request.POST)
        print("hello")
        if data.is_valid():
            # a = data.cleaned_data['username']
            # b = data.cleaned_data['email']
            a= data.cleaned_data['BUDGET'] 
            b = data.cleaned_data['BODY_TYPE']
            c =data.cleaned_data['SEATING_TYPE']
            d = data.cleaned_data['MILEAGE']

            data = query.get_query(a,b,c,d)
            print(data)
            # fun(a,b)
            return HttpResponseRedirect('/submit')
            
        else:
            print("data is invalid")

    
    fr = InputForm()
    return render(request, "sample.html", {'fm' : fr})
    #return render(request, 'customer.html')

def submit(request):
    if request.method == 'POST':
        print("Hello")
    return render(request, 'submit.html')
