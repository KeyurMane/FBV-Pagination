from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Product

def index(request):
    prod_list = Product.objects.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(prod_list, 5)
    try:
        prod = paginator.page(page)
    except PageNotAnInteger:
        prod = paginator.page(1)
    except EmptyPage:
        prod = paginator.page(paginator.num_pages)

    return render(request, 'prod_list.html', { 'prod': prod })
