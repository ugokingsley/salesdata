from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from .models import *
from .forms import *
from django.db.models import Count
from django.views.generic.edit import CreateView 
from django.urls import reverse_lazy



class SalesDataCreate(CreateView): 
    # specify the model for create view 
    model = SalesData 
    form_class = SalesDataForm
    success_url = reverse_lazy('index')
    template_name = 'sales/sales_create.html'





def mostfrequentitem(request):
    list1 = SalesData.objects.values('description').annotate(c=Count('description')).order_by('-c')[:1]
    context = {
        "list1": list1,
    }
    return render(request, 'sales/most-frequent-item.html', context)


def frequentsales(request):
    list1 = SalesData.objects.values('description').annotate(c=Count('description')).order_by('-c')
    context = {
        "list1": list1,
    }
    return render(request, 'sales/frequent-sales.html', context)


def index(request):
    list1 = SalesData.objects.all().order_by('-id')
    page = request.GET.get('page', 1)
    # query = request.GET.get("q")
    '''
    if query:
        list1 = list1.filter(
            Q(description__icontains=description) |
            Q(stockcode__icontains=stockcode)
        ).distinct()
    '''

    paginator = Paginator(list1, 35)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)
    context = {
        "list1": list1,
        "users": users,
    }
    return render(request, 'sales/index.html', context)

